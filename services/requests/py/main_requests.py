"""
This file is called from systemd service
"""

from flask import Flask
from flask_cors import CORS
from requests.setup_endpoints import setup_enpoints


# def setup_app(app):
#     @app.route("/")
#     def home():
#         return render_template("index.html")
#
#     @app.route("/login", methods=["POST", "GET"])
#     def login():
#         if request.method == "POST":
#             _user = request.form["nm"]
#             return redirect(url_for("user", usr=_user))
#         else:
#             return render_template("login.html")
#
#     @app.route("/<usr>")
#     def bounce(usr):
#         return f"<h1>{usr}</h1>"
#
#     @app.route('/post/msg/<msg>', methods=['POST'])
#     def add_message(msg):
#         return jsonify({"message": loads(msg)})
#

def requests_app(config_dir):
    app = Flask(__name__)
    CORS(app)

    setup_enpoints(app=app, config_dir=config_dir)

    return app


if __name__ == '__main__':
    _config_dir = "../../../config"

    _app = requests_app(config_dir=_config_dir)
    _app.run(host="0.0.0.0", debug=True)
