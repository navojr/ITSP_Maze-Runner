import RPi.GPIO as GPIO
from time import sleep
import sys
import math




dfactor = 15.2
afactor = 1.99

lfactor = 1
ldfactor = 1

sleepTime =0.005
#m1_rightmtr m2_leftmtr True_fwd False_bwd
def move(m1,m2,d1,d2,ang):

    GPIO.setmode(GPIO.BCM)
    direcPin1 = 22
    direcPin2 = 17
    stepPin1 = 23
    stepPin2 = 27

    GPIO.setup(stepPin1,GPIO.OUT)
    GPIO.setup(stepPin2,GPIO.OUT)

    GPIO.setup(direcPin1,GPIO.OUT)
    GPIO.setup(direcPin2,GPIO.OUT)

    if(d1):
        GPIO.output(direcPin1,GPIO.HIGH)
    else:
        GPIO.output(direcPin1,GPIO.LOW)
    if(d2):
        GPIO.output(direcPin2,GPIO.HIGH)
    else:
        GPIO.output(direcPin2,GPIO.LOW)
    steps = (int)(ang/1.8)
    for i in range (0,steps):
        if(m1):
            GPIO.output(stepPin1,GPIO.HIGH)
        if(m2):
            GPIO.output(stepPin2,GPIO.HIGH)
        sleep(sleepTime)
        if(m1):
            GPIO.output(stepPin1,GPIO.LOW)
        if(m2):
            GPIO.output(stepPin2,GPIO.LOW)
        sleep(sleepTime)

def moveOne(m,dist,direc):
    angle = dfactor * dist
    if(m and direc):
        move(True,False,True,False,angle)
    elif(m and (not direc)):
        move(True,False,False,False,angle)
    elif((not m) and direc):
        move(False,True,False,True,angle)
    else:
        move(False,True,False,False,angle)


def forward(dist,reverse=False):
    angle = dfactor * dist
    if(not reverse):
        move(True,True,True,True,angle)
    else:
        move(True,True,False,False,angle)

def turn(turnAngle,direc):
	angle = afactor * turnAngle
	if(direc):
		move(True,True,True,False,angle)
	else:
		move(True,True,False,True,angle)

def moveLaterally(dist,direc):
    d = lfactor*14.7*(math.acos(1-dist/14.7))
    distance = 14.7*math.sin(d/14.7)
    if(direc):
        moveOne(True,d,False)
        sleep(0.2)
        moveOne(False,d,False)
        sleep(0.2)
        forward(distance)
    else:
        moveOne(False,d,False)
        sleep(0.2)
        moveOne(True,d,False)
        sleep(0.2)
        forward(distance)

def go_left_laterally(offset):
    moveLaterally(offset,True)
def go_right_laterally(offset):
    moveLaterally(offset,False)
def turnleft_90():
    turn(90,True)
def turnright_90():
    turn(90,False)
def turn_180():
    turn(180,True)
def turn_right(angle):
    turn(angle,False)
def turn_left(angle):
    turn(angle,True)

#moveLaterally(2,True)
#moveOne(False,7,False)
#moveLaterally(1,True)
#turn(90,False)
#forward(5, True)
#forward(7.5)
#sleep(1)
#turn_180()
#forward(8)
#moveOne(True,360,False)
GPIO.cleanup()

