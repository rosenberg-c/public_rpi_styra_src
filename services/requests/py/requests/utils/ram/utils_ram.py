from flask import Flask, jsonify

from requests.support import UTILS_ENDPOINT
from requests.utils.ram.hardware_ram_status import GetRamStatusRpi


def endpoint_ram(app: Flask):
    @app.route(UTILS_ENDPOINT + "/ram")
    def request_ram():
        val = GetRamStatusRpi().ret_info()

        return jsonify(val)
