import json

from flask import Flask, jsonify, request

from requests.backlight.config.validate_json import validate
from requests.backlight.config.get_request_config import convert_dict_to_class
from requests.support import BACKLIGHT_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform
from tools_lib.lib.user_sys.file_system import write


def validate_write(config_dir):
    if validate(request.get_json()):
        config_class = convert_dict_to_class(request.get_json())
        if OSPlatform.is_mac():
            print(json.dumps(config_class.__dict__, indent=2))
        if OSPlatform.is_linux():
            write(json.dumps(config_class.__dict__, indent=2), config_dir + "/backlight/backlight_config.json")
        return jsonify(config_class.__dict__)
    return jsonify(None)


def endpoint_backlight_config_post(app: Flask, config_dir):
    @app.route(BACKLIGHT_ENDPOINT + "/config/<data>", methods=["POST"])
    def request_delta_config_post(data):
        if request.method == "POST":
            if data == "data":
                return validate_write(config_dir)
        return jsonify(None)
