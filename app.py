from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    comments = ["Great post!", "Thanks for sharing.", "Very informative."]
    return render_template("index.html", name="kajetan", user="John", comments=comments)


if __name__ == "__main__":
    app.run(debug=True)
