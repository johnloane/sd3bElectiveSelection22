from flask import Flask, render_template, request

app = Flask(__name__)

ELECTIVES = [
    "Smart Technology",
    "Artificial Intelligence",
    "Immersive Technologies",
    "Service Oriented Architecture"
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():


app.run(debug=True)