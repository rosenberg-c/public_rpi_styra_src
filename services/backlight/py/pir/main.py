#!/usr/bin/env python
# based on https://github.com/cowboysdude/Pir-Sensor/blob/master/pir.py

import subprocess
import sys
import time

from lib.gpio_scan import RPIG

SHUTOFF_DELAY = 30  # seconds

pin_17 = RPIG(pin=17)


def main():
    turned_off = False
    last_motion_time = time.time()

    while True:

        if pin_17.is_on():
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + SHUTOFF_DELAY):
                turned_off = True
                turn_off()
        time.sleep(.1)


def turn_on():
    print("MONITOR ON")
    subprocess.call("vcgencmd display_power 1", shell=True)
    # subprocess.call("xset s reset ; tvservice -p ; xset dpms force on", shell=True)
    # subprocess.call("tvservice -p", shell=True)
    # subprocess.call("sh /home/pi/Pir-sensor/monitor_on.sh", shell=True)


def turn_off():
    print("MONITOR OFF")
    subprocess.call("vcgencmd display_power 0", shell=True)
    # subprocess.call("sh /home/pi/Pir-sensor/monitor_off.sh", shell=True)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pin_17.cleanup()
