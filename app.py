from flask import Flask, session
from bunny import bunny

app = Flask(__name__)


@app.route("/")
def index():
    session["bunny_type"] = bunny.START


# @app.route("/bunny", methods=["GET", "POST"])
# def bunny():
