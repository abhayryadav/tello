# dronecontroll
import controll
controll.init()
from djitellopy import tello
from time import sleep

mytello = tello.Tello()
mytello.connect()
print(mytello.get_battery())

def keyboardinput():
    lr , fb , ud , yaw =0,0,0,0
    speed = 3

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
    sleep(0.05)