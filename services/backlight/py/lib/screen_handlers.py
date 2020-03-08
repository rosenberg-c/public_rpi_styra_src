import os
import json

ADAFRUIT_TYPE = "adafruit3_5"
HDMI_TYPE = "hdmi"
SCREEN_TYPES = f'["{ADAFRUIT_TYPE}","{HDMI_TYPE}"]'


class HDMICommands:
    def __init__(self):
        self.base_hdmi = "vcgencmd display_power "

    def on(self):
        return self.base_hdmi + "1"

    def off(self):
        return self.base_hdmi + "0"


class ADAFRUITCommands:
    ADAFRUIT_URL = "/sys/class/backlight/soc:backlight/brightness"

    def __init__(self):
        self.base_adafruit = f'sudo sh -c '

    def on(self):
        return self.base_adafruit + f'"echo 1 > {self.ADAFRUIT_URL}"'

    def off(self):
        return self.base_adafruit + f'"echo 0 > {self.ADAFRUIT_URL}"'


def screens(screen_types: list, s_type: str):
    if s_type in screen_types:
        return True
    return False


def run_on_script():
    if screens(screen_types=json.loads(SCREEN_TYPES), s_type=ADAFRUIT_TYPE):
        os.system(ADAFRUITCommands().on())

    if screens(screen_types=json.loads(SCREEN_TYPES), s_type=HDMI_TYPE):
        os.system(HDMICommands().on())


def run_off_script():
    if screens(screen_types=json.loads(SCREEN_TYPES), s_type=ADAFRUIT_TYPE):
        os.system(ADAFRUITCommands().off())
    if screens(screen_types=json.loads(SCREEN_TYPES), s_type=HDMI_TYPE):
        os.system(HDMICommands().off())


def main():
    run_off_script()


if __name__ == '__main__':
    main()
