import os

from flask import Flask, jsonify, request

from requests.support import ENERGENIE_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform


def restart_energenie_service():
    cmd = "sudo systemctl restart energenie.service"
    if OSPlatform.is_mac():
        print(cmd)
        return
    if OSPlatform.is_linux():
        os.system(cmd)
        return
    raise NotImplementedError("Restart service for this OS is not implemented")


def endpoint_energenie_restart_service(app: Flask):
    # @app.route('/post/msg/<msg>', methods=['POST'])
    @app.route(ENERGENIE_ENDPOINT + "/restart", methods=["GET"])
    def request_energenie_restart_get():
        if request.method == "GET":
            restart_energenie_service()
            return jsonify(True)

        return jsonify(None)
