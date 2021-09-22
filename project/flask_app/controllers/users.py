from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash, session, render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.task import Task
from flask_app.controllers import tasks, notes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if not User.get_one_username(request.form):
        return redirect("/")
    user = User.get_one_username(request.form)
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return redirect("/")
    session['user_id'] = user.id
    return redirect("/dashboard")

@app.route("/register", methods=["POST"])
def register_user():
    if not User.validate_reg(request.form):
        return redirect("/")
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "username" : request.form['username'],
        "email": request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(data)
    session['user_id'] = id
    return redirect('/dashboard')

@app.route("/dashboard")
def show_dashboard():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : session['user_id']
    }
    user = User.get_one_id(data)
    tasks = Task.get_user_tasks(data)
    return render_template("dashboard.html", user=user, tasks=tasks)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")