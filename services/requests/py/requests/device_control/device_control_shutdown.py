import os

from flask import Flask, jsonify, request

from requests.support import DEVICE_ENDPOINT
from tools_lib.lib.os_platform.os_platform import OSPlatform


def _shutdown(sleep):
    cmd = f"nohup sudo -b bash -c 'sleep {sleep}; shutdown -h now' &> /dev/null; "
    if OSPlatform.is_linux():
        os.system(cmd)
    print(f"cmd: {cmd}")


def endpoint_shutdown(app: Flask):
    @app.route(DEVICE_ENDPOINT + "/shutdown/<data>", methods=["POST"])
    def request_shutdown(data):
        if request.method == "POST":
            if data == "data":
                _shutdown(request.get_json()["sleep"])
                return jsonify(True)

        return jsonify(None)
