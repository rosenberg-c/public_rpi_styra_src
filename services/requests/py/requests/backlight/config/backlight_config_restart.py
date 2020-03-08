import os

from flask import Flask, jsonify, request

from requests.support import BACKLIGHT_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform


def restart_backlight_service():
    cmd = "sudo systemctl restart backlight.service"
    if OSPlatform.is_mac():
        print(cmd)
        return
    if OSPlatform.is_linux():
        os.system(cmd)
        return
    raise NotImplementedError("Restart service for this OS is not implemented")


def endpoint_backlight_restart_service(app: Flask):
    # @app.route('/post/msg/<msg>', methods=['POST'])
    @app.route(BACKLIGHT_ENDPOINT + "/restart", methods=["GET"])
    def request_backlight_restart():
        if request.method == "GET":
            restart_backlight_service()
            return jsonify(True)

        return jsonify(None)
