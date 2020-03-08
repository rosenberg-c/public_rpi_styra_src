import json

from tools_lib.lib.user_sys.file_system import read


def convert_json_path(fpath):
    return json.loads(read(fpath))


def convert_json_obj(fpath):
    return json.loads(fpath)


class Config:
    def __init__(self, auto_on, auto_off, disable_from, enable_from, update_cycle, ignore_gpio, name):
        self.auto_on = auto_on
        self.auto_off = auto_off
        self.disable_from = disable_from
        self.enable_from = enable_from
        self.update_cycle = update_cycle
        self.ignore_gpio = ignore_gpio
        self.name = name


def convert_dict_to_class(j_dict: dict):
    return Config(
        auto_on=j_dict["auto_on"],
        auto_off=j_dict["auto_off"],
        disable_from=j_dict["disable_from"],
        enable_from=j_dict["enable_from"],
        update_cycle=j_dict["update_cycle"],
        ignore_gpio=j_dict["ignore_gpio"],
        name=j_dict["name"]
    )
