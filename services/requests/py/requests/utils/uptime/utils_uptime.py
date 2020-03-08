from datetime import datetime, timedelta

from flask import Flask, jsonify

from requests.support import UTILS_ENDPOINT
from tools_lib.lib.user_sys.subproc import read_sub

YMD_format = '%Y-%m-%d'
HMS_format = '%H:%M:%S'


def date_from_string(string: str, t_format: str = YMD_format + ' ' + HMS_format) -> datetime:
    return datetime.strptime(string, t_format)


def endpoint_upptime(app: Flask):
    @app.route(UTILS_ENDPOINT + "/uptime")
    def request_uptime():
        val = read_sub(["uptime", "-s"]).strip()

        now = datetime.now()
        as_sec = (now - date_from_string(val)).total_seconds()
        return jsonify(str(timedelta(seconds=as_sec)).split(".")[0])
        # if as_sec < 60:
        #     return jsonify(f"{int(as_sec)} s")
        # if as_sec < 3600:
        #     return jsonify(f"{int(as_sec / 60)} m")
        #
        # return jsonify(f"{int(as_sec / 60 / 60)} h")
