from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash, session, render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.question import Question
from flask_app.models.answer import Answer
from flask_app.controllers import questions, answers

@app.route('/')
def login():
    return render_template("index.html")


@app.route('/register_user', methods=["POST"])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/')
    data = {
        "username" : request.form['username'],
        "email": request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.create_user(data)
    session['user_id'] = id
    return redirect('/userpage')


@app.route('/login', methods=["POST"])
def user_login():
    user = User.get_one_email(request.form)
    if not user:
        flash("Invalid login", "no_user")
        return redirect('/')
    print(user)
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/userpage')


@app.route('/userpage')
def render_userpage():
    if 'user_id' not in session: 
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    user = User.get_one_id(data)
    questions = Question.get_all_questions()
    return render_template("userpage.html", user=user, questions=questions)


@app.route('/logout')
def user_quit():
    session.clear()
    return redirect('/')