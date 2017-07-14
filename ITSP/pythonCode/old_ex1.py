
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 17
Motor1B = 23
Motor2A = 27
Motor2B = 22
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)

def pwm(y, one, two, t, smooth = True):
    if one:
        m1a = Motor1A
        m1b = Motor1B
    else:
        m1b = Motor1A
        m1a = Motor1B
    if two:
        m2a = Motor2A
        m2b = Motor2B
    else:
        m2b = Motor2A
        m2a = Motor2B
    i = 0
    if smooth:
        y /= 100
        x = 0.1
    else:
        y /= 100
        x = y
    while i < t:
        GPIO.output(m1a,GPIO.HIGH)
        GPIO.output(m1b,GPIO.LOW)
        GPIO.output(m2a,GPIO.LOW)
        GPIO.output(m2b,GPIO.HIGH)
        sleep(x * 0.01)
        GPIO.output(m1a,GPIO.LOW)
        GPIO.output(m1b,GPIO.LOW)
        GPIO.output(m2a,GPIO.LOW)
        GPIO.output(m2b,GPIO.LOW)
        sleep(0.01*(1 - x))
        i += 1
        if smooth:
            if x < y:
                x += 0.005

def single_pwm(pwm,motor_bool,dir,time):
    if motor_bool:
        if dir:
            ma = Motor1A
            mb = Motor1B
        else:
            ma = Motor1B
            mb = Motor1A
    else:
        if dir:
            mb = Motor2A
            ma = Motor2B
        else:
            mb = Motor2B
            ma = Motor2A
    pwm /= 100
    i=0
    while i < time:
        GPIO.output(ma,GPIO.HIGH)
        GPIO.output(mb,GPIO.LOW)
        sleep(pwm*0.01)
        GPIO.output(ma,GPIO.LOW)
        GPIO.output(mb,GPIO.LOW)
        sleep(0.01*(1 - pwm))
        i+=1
#pwm(50,True,False,150,True)
"""single_pwm(35,True,True,1000)"""
"""single_pwm(35,False,False,300)"""

"""
pwm(40, True, True, 275)
pwm(50, False, True, 130, False)
pwm(40, True, True, 200)
pwm(50, False, True, 130, False)
"""
"""
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
sleep(2)"""
GPIO.cleanup()
