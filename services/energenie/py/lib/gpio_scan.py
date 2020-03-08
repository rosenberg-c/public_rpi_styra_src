#!/usr/bin/env python
# based on https://github.com/cowboysdude/Pir-Sensor/blob/master/pir.py


# import RPi.GPIO as GPIO


class RPIG:
    def __init__(self, pin):
        self.pin = pin

        self._init()

    def _init(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        pass

    def is_on(self):
        # if not GPIO.input(self.pin):
        # if not GPIO.input(self.pin):
        #     return True
        return False

    def cleanup(self):
        # GPIO.cleanup()
        pass
