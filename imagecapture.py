# imagecapture
import controll
controll.init()
from djitellopy import Tello
import cv2
import time
import collections
from time import sleep

mytello = Tello()
mytello.connect()
mytello.streamon()
time.sleep(5) 
print(mytello.get_battery())

def keyboardinput():
    lr , fb , ud , yaw =0,0,0,0
    speed = 50

    if controll.keyy("LEFT"): lr = -speed
    elif controll.keyy("RIGHT"): lr = speed

    if controll.keyy("UP"): fb = speed
    elif controll.keyy("DOWN"): fb = -speed

    if controll.keyy("w"): ud = speed
    elif controll.keyy("s"): ud = -speed

    if controll.keyy("a"): yaw = speed
    elif controll.keyy("d"): yaw = -speed

    if controll.keyy("l"): mytello.land()
    if controll.keyy("t"): mytello.takeoff()

    return [lr,fb,ud,yaw]


while True:
    commands = keyboardinput()
    mytello.send_rc_control(commands[0],commands[1],commands[2],commands[3])

    frame = mytello.get_frame_read().frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    bright_frame = cv2.convertScaleAbs(rgb_frame, alpha=1.2, beta=30)
    cv2.imshow('Tello Video Stream - RGB Adjusted', bright_frame)
    sleep(0.05)