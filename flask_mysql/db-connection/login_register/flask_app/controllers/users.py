from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/create', methods=["POST"])
def create():
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email": request.form['email'],
        "password" : pw_hash,
    }
    User.create_user(data)
    return redirect('/welcome')

@app.route('/login', methods=["POST"])
def login():
    if not User.locate_user(request.form):
        return redirect('/')
    user = User.locate_user(request.form)
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if session['user_id'] == 0:
        flash("Not logged in", 'no_user')
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    user = User.locate_by_id(data)
    return render_template("welcome_user.html", user=user)

@app.route()
def pw():
    pass

@app.route('/logout')
def logout():
    session['user_id']=0 #this removes the id only. 
    return redirect('/')