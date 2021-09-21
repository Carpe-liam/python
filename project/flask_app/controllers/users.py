from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash, session, render_template, redirect, request
from flask_app.models.user import User

@app.route("/")
def login():
    return render_template("index.html")