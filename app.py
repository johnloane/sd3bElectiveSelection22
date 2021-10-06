from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
mysql_env = os.getenv('MYSQL_USER')
print(mysql_env)
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sd3b_elective'

mysql = MySQL(app)

STUDENTS_CHOICES = {}

ELECTIVES = [
    "Smart Technology",
    "Artificial Intelligence",
    "Immersive Technologies",
    "Service Oriented Architecture"
]


@app.route("/")
def index():
    return render_template("index.html", electives=ELECTIVES)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    elective = request.form.get("elective")
    if not name or not elective or elective not in ELECTIVES:
        return render_template("failure.html")
    STUDENTS_CHOICES[name]=elective
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=STUDENTS_CHOICES)


app.run(debug=True)