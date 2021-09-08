from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template("read.html", users=users)

@app.route('/users/new')
def create():
    return render_template("create.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<int:userID>/edit')
def edit(userID):
    data = {
        'userID' : userID,
    }
    user = User.get_one(data)
    return render_template("edit.html", user = user)

@app.route('/update/<int:userID>', methods=["POST"])
def update(userID):
    data = {
        'userID' : userID,
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.edit(data)
    return redirect(f'/users/{userID}')

@app.route('/users/<int:userID>')
def show_info(userID):
    data = {
        'userID': userID
    }
    user = User.get_one(data)
    return render_template("show_info.html", user = user)

@app.route('/users/<int:userID>/destroy')
def delete(userID):
    data = {
        'userID' : userID
    }
    User.delete(data)
    return redirect('/users')