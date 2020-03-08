from flask import Flask, jsonify

from requests.support import UTILS_ENDPOINT


def endpoint_online(app: Flask):
    @app.route(UTILS_ENDPOINT + "/online")
    def request_online():
        return jsonify(True)
