import os

from flask import Flask, jsonify, request
from requests.energenie.config.get_request_config import convert_dict_to_class, convert_json_path, Config
from requests.support import ENERGENIE_ENDPOINT


def validate_read(pa):
    return jsonify(convert_dict_to_class(convert_json_path(pa)).__dict__)


def endpoint_energenie_config_get(app: Flask, config_dir):
    @app.route(ENERGENIE_ENDPOINT + "/config", methods=["GET"])
    def request_energenie_delta_config_get():
        if request.method == "GET":

            _path = config_dir + "/energenie/energenie_config.json"
            if os.path.isfile(_path):
                return validate_read(_path)

            # return validate_read(config_dir + "/energenie_config_default.json")
            return jsonify(Config(
                auto_on=False,
                auto_off=False,
                disable_from="00:00:00",
                enable_from="00:00:00",
                update_cycle=6,
                ignore_gpio=False,
                name="Default"
            ).__dict__)
        return jsonify(None)
