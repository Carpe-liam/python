from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_app.controllers import messages

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/create', methods=["POST"])
def create():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(data)
    session['user_id'] = id
    return redirect('/welcome')

@app.route('/login', methods=["POST"])
def login():
    if not User.locate_user(request.form):
        return redirect('/')
    if 'user_id' not in session:
        flash("please login", "login")
        return redirect('/')
    user = User.locate_user(request.form)
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    print(session['user_id'])
    user = User.locate_by_id(data)
    messages = Message.get_user_messages(data)
    userbase= User.get_all()
    return render_template("welcome_user.html", user=user, userbase=userbase, messages=messages)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')