from flask import Flask, jsonify, request

from requests.backlight.on_off.contol import backlight_control
from requests.support import BACKLIGHT_ENDPOINT


def endpoint_backlight_on(app: Flask):
    @app.route(BACKLIGHT_ENDPOINT + "/on/<data>", methods=["POST"], endpoint="on")
    def request_ls(data):
        if request.method == "POST":
            if data == "data":
                backlight_control(request.get_json()["sleep"], "on")
                return jsonify(True)

        return jsonify(None)
