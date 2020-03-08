import json

from flask import Flask, jsonify, request

from requests.energenie.config.validate_json import validate
from requests.energenie.config.get_request_config import convert_dict_to_class
from requests.support import ENERGENIE_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform
from tools_lib.lib.user_sys.file_system import write


def validate_write(config_dir):
    if validate(request.get_json()):
        config_class = convert_dict_to_class(request.get_json())
        if OSPlatform.is_mac():
            print(json.dumps(config_class.__dict__, indent=2))
        if OSPlatform.is_linux():
            write(json.dumps(config_class.__dict__, indent=2), config_dir + "/energenie/energenie_config.json")
        return jsonify(config_class.__dict__)
    print("Did not validate json")
    return jsonify(None)


def endpoint_energenie_config_post(app: Flask, config_dir):
    @app.route(ENERGENIE_ENDPOINT + "/config/<data>", methods=["POST"])
    def request_energenie_delta_config_post(data):
        if request.method == "POST":
            if data == "data":
                return validate_write(config_dir)
        return jsonify(None)
