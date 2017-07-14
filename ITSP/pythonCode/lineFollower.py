import cv2
import numpy as np
import time
from detection import *
from ex2 import *
import math
from picamera import PiCamera
camera = PiCamera()

def startCam():
    camera.start_preview()
    time.sleep(1)

def captureImg():
    camera.capture('runimg.jpg')
    img = cv2.imread('runimg.jpg', 1)
    return img

def stopCam():
    camera.stop_preview()

"""
def correctAngle(ang):
    print("angle", ang)
    if math.fabs(ang) < 30:
        if ang > 0:
            t = 4.3 * ang / 10
            pwm(50, True, False, t, False)
        else:
            t = 4.1 * ang / 10
            pwm(50, False, True, t, False)
    else:
        if ang > 0:
            t = 42 * ang / 90
            pwm(50, True, False, t, False)
        else:
            t = 45 * ang / 90
            pwm(50, False, True, t, False)"""

def correctAngle(ang):
    print("angle correction", ang)
    if ang > 0:
        turn_right(ang)
    else:
        turn_left(-ang)

def moveForward(dist = 300):
    dist = dist * 7 / 420
    print("moving", dist)
    if dist > 0:
        forward(dist)
    else:
        print("cannot move Backward now")

def correctOffset(dis):
    dis = dis * 11 / 720
    print("offset correction", dis)
    if dis > 0:
        go_right_laterally(1)
    else:
        go_left_laterally(1)


if __name__ == "__main__":
    startCam()
    while True:
        im = captureImg()
        ang = getAngle(im.copy())
        print("angle", ang)

        while math.fabs(ang) > 6:
            correctAngle(ang)
            im = captureImg()
            ang = getAngle(im.copy())
            print("angle", ang)

 #       im = captureImg()
        off = getOffset(im.copy())
        print("off", off)

        while math.fabs(off) > 220:
            correctOffset(off)
            print("off", off)
            im = captureImg()
            ang = getAngle(im.copy())
            print("angle", ang)

            while math.fabs(ang) > 6:
                correctAngle(ang)
                print("angle", ang)
                im = captureImg()
                ang = getAngle(im.copy())
            off = getOffset(im.copy())

#        im = captureImg()
        ang = getAngle(im.copy())
        print("angle", ang)
        while math.fabs(ang) > 6:
            correctAngle(ang)
            print("angle", ang)
            im = captureImg()
            ang = getAngle(im.copy())
        im = captureImg()
#        cv2.imshow("image", im)
#        cv2.waitKey(1000)
        xJ = getJunction(im.copy())
        print("xjxjxj", xJ)
        junc = xJ[0]
        print("junc", junc)
        if junc == -1:
#            GPIO.cleanup()
            break
        elif junc == 0:
            moveForward(300)
        elif xJ[1][1] < -100:
            moveForward(75)
        else:
            if (junc == 1) or (junc == 3):
                moveForward()
                moveForward()
                turnleft_90()
                moveForward()
            else:
                moveForward()
                moveForward()
                turnright_90()
                moveForward()
    stopCam()
