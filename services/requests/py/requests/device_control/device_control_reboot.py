import os

from flask import Flask, jsonify, request

from requests.support import DEVICE_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform


def _reboot(sleep):
    cmd = f"nohup sudo -b bash -c 'sleep {sleep}; reboot' &> /dev/null; "
    if OSPlatform.is_linux():
        os.system(cmd)
    print(f"cmd: {cmd}")


def endpoint_reboot(app: Flask):
    @app.route(DEVICE_ENDPOINT + "/reboot/<data>", methods=["POST"])
    def request_reboot(data):
        if request.method == "POST":
            if data == "data":
                _reboot(request.get_json()["sleep"])
                return jsonify(True)

        return jsonify(None)
