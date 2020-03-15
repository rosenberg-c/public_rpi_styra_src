"""
This file is called from systemd service
"""
import os
import time
from datetime import timedelta

from handle_socket import HandleSocket
from lib.get_energenie_config import json_to_config, read_json
from lib.gpio_scan import RPIG
from main_function import main_on_off_wrapper
from tools_lib.lib.time_delta.between_hours import get_date_now
from lib.energenie_handlers import run_off_script, run_on_script


def main(auto_on: bool, auto_off: bool, disable_from, enable_from, update_cycle, ignore_gpio):
    pin_5a = RPIG(pin=5)
    pin_6b = RPIG(pin=6)

    next_update = get_date_now() + timedelta(seconds=update_cycle)
    handle_socket = HandleSocket(on=run_on_script, off=run_off_script)
    while True:
        main_on_off_wrapper(
            disable_from=disable_from,
            enable_from=enable_from,
            auto_on=auto_on,
            auto_off=auto_off,
            handle_socket=handle_socket
        )

        print("Sleep" + str(update_cycle))
        time.sleep(update_cycle)
        print("End final")


def get_json(config_path, default_path):
    if os.path.isfile(config_path):
        return json_to_config(j_content=read_json(f_path=config_path))
    return json_to_config(j_content=read_json(f_path=default_path))


if __name__ == '__main__':
    _config_path = "../../config/energenie"
    json_path = _config_path + "/energenie_config.json"
    json_path_default = _config_path + "/energenie_config_default.json"

    energenie_config = get_json(config_path=json_path, default_path=json_path_default)

    main(
        auto_on=energenie_config.auto_on,
        auto_off=energenie_config.auto_off,
        disable_from=energenie_config.disable_from,
        enable_from=energenie_config.enable_from,
        update_cycle=energenie_config.update_cycle,
        ignore_gpio=energenie_config.ignore_gpio
    )
