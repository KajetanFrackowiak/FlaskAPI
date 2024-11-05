from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
import pytz

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route("/")
def index():
    utc_timezone = pytz.UTC
    current_time = datetime.now(utc_timezone)
    print(f"Current Time: {current_time}")  # Add this line to debug
    return render_template("index.html", current_time=current_time)


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
