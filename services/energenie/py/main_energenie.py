"""
This file is called from systemd service
"""
import os
import time
from datetime import timedelta

from lib.energenie_handlers import run_off_script, run_on_script
from lib.get_energenie_config import json_to_config, read_json
from lib.gpio_scan import RPIG
from lib.main_delta import within_delta
from tools_lib.lib.time_delta.between_hours import get_date_now


def _flip(val):
    val ^= True
    return val


def _handle_screen(should_be_on, auto_on, auto_off):
    if should_be_on:
        if auto_on:
            run_on_script(socket=1)
    else:
        if auto_off:
            run_off_script(socket=1)


def _while_did_press(on_active, pin, should_be_on, handler, cycle_t):
    if on_active:
        should_be_on = _flip(should_be_on)
        handler(should_be_on)
        while on_active:
            did_use = pin.is_on()
            on_active = _flip(did_use)
            if did_use:
                should_be_on = _flip(should_be_on)
                handler(should_be_on)
            if get_date_now() > cycle_t:
                on_active = False
            time.sleep(0.1)


def _on_flip_state(on_active, pin, handler):
    if on_active:
        handler(False)
        while pin.is_on():
            time.sleep(0.1)


def main(auto_on: bool, auto_off: bool, disable_from, enable_from, update_cycle, ignore_gpio):
    pin_5a = RPIG(pin=5)
    pin_6b = RPIG(pin=6)

    next_update = get_date_now() + timedelta(seconds=update_cycle)
    should_be_on = True

    while True:
        if not ignore_gpio:
            _while_did_press(
                on_active=pin_5a.is_on(),
                pin=pin_5a,
                should_be_on=should_be_on,
                handler=_handle_screen,
                cycle_t=next_update
            )

            flip_state = pin_6b.is_on()
            if flip_state:
                _on_flip_state(
                    on_active=pin_6b.is_on(),
                    pin=pin_6b,
                    handler=_handle_screen
                )
                should_be_on = within_delta(
                    disable_from=disable_from,
                    enable_from=enable_from,
                    auto_on=auto_on,
                    auto_off=auto_off
                )
                _handle_screen(should_be_on=should_be_on, auto_on=auto_on, auto_off=auto_off)

        should_be_on = within_delta(
            disable_from=disable_from,
            enable_from=enable_from,
            auto_on=auto_on,
            auto_off=auto_off
        )
        if get_date_now() > next_update:
            _handle_screen(should_be_on=should_be_on, auto_on=auto_on, auto_off=auto_off)
            next_update = get_date_now() + timedelta(seconds=update_cycle)

        time.sleep(0.1)
        print("End")


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
