# import math
# from djitellopy import Tello
# import cv2
# import time
# from time import sleep
# import controll  # Ensure this module exists and is correctly implemented
# controll.init()
# import numpy as np
#
# # params ###############
# xyspeed = 117 / 10
# angularspeed = 360 / 10
# interval = 0.25
# disp = xyspeed * interval
# rotation = angularspeed * interval
# # ######################
# x, y = 200, 200
# angle = 0
# yawangle = 0  # Initialize yawangle
#
# mytello = Tello()
# mytello.connect()
# mytello.streamon()
# time.sleep(5)
# print(mytello.get_battery())
#
# def keyboardinput():
#     lr, fb, ud, yaw = 0, 0, 0, 0
#     speed = 50
#     d = 0
#     global angle, x, y, yawangle  # Declare globals
#
#     if controll.keyy("LEFT"):
#         lr = -speed
#         d = disp
#         angle = -180
#     elif controll.keyy("RIGHT"):
#         lr = speed
#         d = -disp
#         angle = 180
#     if controll.keyy("UP"):
#         fb = speed
#         d = disp
#         angle = 270
#     elif controll.keyy("DOWN"):
#         fb = -speed
#         d = -disp
#         angle = -90
#     if controll.keyy("w"):
#         ud = speed
#     elif controll.keyy("s"):
#         ud = -speed
#
#     if controll.keyy("a"):
#         yaw = speed
#         yawangle += rotation
#     elif controll.keyy("d"):
#         yaw = -speed
#         yawangle -= rotation
#     if controll.keyy("l"):
#         mytello.land()
#     if controll.keyy("t"):
#         mytello.takeoff()
#
#     # Update angle with yaw
#     # angle += yawangle
#     # Update x and y positions
#     x += int(disp * math.cos(math.radians(angle)))
#     y += int(disp * math.sin(math.radians(angle)))
#
#     return [lr, fb, ud, yaw, x, y]
#
# def drawer(img, x, y):
#     cv2.circle(img, (x, y), 10, (0, 0, 255), cv2.FILLED)
#
# while True:
#     commands = keyboardinput()
#     mytello.send_rc_control(commands[0], commands[1], commands[2], commands[3])
#
#     frame = mytello.get_frame_read().frame
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     bright_frame = cv2.convertScaleAbs(rgb_frame, alpha=1.2, beta=30)
#     cv2.imshow('Tello Video Stream - RGB Adjusted', bright_frame)
#
#     track_image = np.zeros((400, 400, 3), np.uint8)  # Create blank image
#     drawer(track_image, commands[4], commands[5])  # Draw the tracked position
#     cv2.imshow("track", track_image)
#     cv2.waitKey(1)
import math
from djitellopy import Tello
import cv2
import time
from time import sleep
import controll  # Ensure this module exists and is correctly implemented
controll.init()
import numpy as np

# params ###############
xyspeed = 117 / 10
angularspeed = 360 / 10
interval = 0.25
disp = xyspeed * interval
rotation = angularspeed * interval
# ######################
x, y = 200, 200
angle = 0
yawangle = 0  # Initialize yawangle
points=[]
mytello = Tello()
mytello.connect()
mytello.streamon()
time.sleep(5)
print(mytello.get_battery())

def keyboardinput():
    lr, fb, ud, yaw = 0, 0, 0, 0
    speed = 50
    d = 0
    global angle, x, y, yawangle  # Declare globals

    # Movement flag to check if a directional key is pressed
    moved = False

    if controll.keyy("LEFT"):
        lr = -speed
        d = disp
        angle = -180
        moved = True
    elif controll.keyy("RIGHT"):
        lr = speed
        d = -disp
        angle = 0
        moved = True
    if controll.keyy("UP"):
        fb = speed
        d = disp
        angle = 270
        moved = True
    elif controll.keyy("DOWN"):
        fb = -speed
        d = -disp
        angle = 90
        moved = True
    if controll.keyy("w"):
        ud = speed
    elif controll.keyy("s"):
        ud = -speed

    if controll.keyy("a"):
        yaw = speed
        yawangle += rotation
    elif controll.keyy("d"):
        yaw = -speed
        yawangle -= rotation

    if controll.keyy("l"):
        mytello.land()
    if controll.keyy("t"):
        mytello.takeoff()

    time.sleep(0.25)
    # Update x and y positions only if moved
    if moved:
        x += int(disp * math.cos(math.radians(angle)))
        y += int(disp * math.sin(math.radians(angle)))

    return [lr, fb, ud, yaw, x, y]

def drawer(img, points):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 1, (0, 0, 255), cv2.FILLED)
        # Display the coordinate of the last point in meters
    if points:
        last_point = points[-1]
        x_meters = (last_point[0] - 500) / 100  # Convert x-coordinate from pixels to meters
        y_meters = (last_point[1] - 500) / 100  # Convert y-coordinate from pixels to meters

        # Display the coordinate text in the bottom-right corner
        text = f'({x_meters:.2f}m, {y_meters:.2f}m)'
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
        text_x = img.shape[1] - text_size[0] - 10
        text_y = img.shape[0] - 10
        cv2.putText(img, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
while True:
    commands = keyboardinput()
    mytello.send_rc_control(commands[0], commands[1], commands[2], commands[3])

    frame = mytello.get_frame_read().frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    bright_frame = cv2.convertScaleAbs(rgb_frame, alpha=1.2, beta=30)
    cv2.imshow('Tello Video Stream - RGB Adjusted', bright_frame)

    track_image = np.zeros((400, 400, 3), np.uint8)  # Create blank image
    points.append([commands[4], commands[5]])
    drawer(track_image, points)  # Draw the tracked position
    cv2.imshow("track", track_image)
    cv2.waitKey(1)
