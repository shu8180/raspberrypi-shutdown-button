#!/usr/bin/env python

import commands
import RPi.GPIO as GPIO
from time import sleep

BUTTON_SHUTDOWN = 21

WAIT_TIME = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_SHUTDOWN, GPIO.IN)

cnt = 0

try:
    while True:
        if GPIO.input(BUTTON_SHUTDOWN) == GPIO.HIGH:
            cnt += WAIT_TIME
            if cnt >= 5:
                commands.getoutput("sudo halt")
                #commands.getoutput("echo test")
        else:
            cnt = 0

        sleep(WAIT_TIME)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

