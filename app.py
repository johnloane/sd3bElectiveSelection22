from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

import os

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")

mail = Mail(app)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
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
    email = request.form.get("email")
    print(email)
    elective = request.form.get("elective")
    if not email or not elective or elective not in ELECTIVES:
        return render_template("failure.html")
    #STUDENTS_CHOICES[email]=elective
    # cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO students(name, elective) VALUES (%s, %s)", (email, elective))
    # mysql.connection.commit()
    # cur.close()
    message = Message("You are registered", recipients=[email])
    mail.send(message)
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    cur = mysql.connection.cursor()
    cur.execute("select name, elective from students")
    registrants = cur.fetchall()
    return render_template("registrants.html", registrants=registrants)


app.run(debug=True)