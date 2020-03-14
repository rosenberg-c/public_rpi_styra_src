"""
This file is called from systemd service
"""
import os
import time
from datetime import timedelta

from lib.get_backlight_config import json_to_config, read_json
from main_function import HandleScreen, off_within_delta, on_outside_delta, main_on_off_wrapper
from pir.main import RPIG
from tools_lib.lib.time_delta.between_hours import get_date_now


def main(auto_on: bool, auto_off: bool, disable_from, enable_from, update_cycle, ignore_gpio):
    pin_5a = RPIG(pin=5)
    pin_6b = RPIG(pin=6)

    next_update = get_date_now() + timedelta(seconds=update_cycle)
    handle_screen = HandleScreen()
    while True:
        main_on_off_wrapper(
            disable_from=disable_from,
            enable_from=enable_from,
            auto_on=auto_on,
            auto_off=auto_off,
            handle_screen=handle_screen
        )

        print("Sleep" + str(update_cycle))
        time.sleep(update_cycle)
        print("End final")


def get_json(config_path, default_path):
    if os.path.isfile(config_path):
        return json_to_config(j_content=read_json(f_path=config_path))
    return json_to_config(j_content=read_json(f_path=default_path))


if __name__ == '__main__':
    _config_path = "../../config/backlight"
    json_path = _config_path + "/backlight_config.json"
    json_path_default = _config_path + "/backlight_config_default.json"

    backlight_config = get_json(config_path=json_path, default_path=json_path_default)

    main(
        auto_on=backlight_config.auto_on,
        auto_off=backlight_config.auto_off,
        disable_from=backlight_config.disable_from,
        enable_from=backlight_config.enable_from,
        update_cycle=backlight_config.update_cycle,
        ignore_gpio=backlight_config.ignore_gpio
    )
