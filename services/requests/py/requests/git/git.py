from flask import Flask, jsonify

from requests.support import GIT_ENDPOINT
from lib.tools import Str
from tools_lib.lib.user_sys.subproc import read_sub


def endpoint_ls(app: Flask):
    @app.route(GIT_ENDPOINT + "/mirror-update")
    def request_ls():
        val = Str.split_to_list(string=read_sub(["ls"]))

        return jsonify(val)

