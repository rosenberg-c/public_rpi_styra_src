from flask import Flask, jsonify

from requests.support import UTILS_ENDPOINT
from requests.utils.temp.temperature import Temperature


def endpoint_temp(app: Flask):
    @app.route(UTILS_ENDPOINT + "/temp")
    def request_temp():
        val = Temperature().return_temp()

        val = val + '\'C'
        return jsonify(val)
