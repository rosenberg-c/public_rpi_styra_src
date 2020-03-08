import json

from tools_lib.lib.user_sys.file_system import read


def read_json(f_path):
    return json.loads(read(f_path))


class EnergenieConfig:
    def __init__(self, auto_on, auto_off, disable_from, enable_from, update_cycle, ignore_gpio, name):
        self.auto_on = auto_on
        self.auto_off = auto_off
        self.disable_from = disable_from
        self.enable_from = enable_from
        self.update_cycle = update_cycle
        self.ignore_gpio = ignore_gpio
        self.name = name


def json_to_config(j_content: dict):
    return EnergenieConfig(
        auto_on=j_content["auto_on"],
        auto_off=j_content["auto_off"],
        disable_from=j_content["disable_from"],
        enable_from=j_content["enable_from"],
        update_cycle=j_content["update_cycle"],
        ignore_gpio=j_content["ignore_gpio"],
        name=j_content["name"]
    )
