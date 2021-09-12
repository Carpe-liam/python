from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.controllers import users

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    user = User.locate_by_id(data)
    return render_template("new_recipe.html", user=user)

@app.route('/recipe/save', methods=["POST"])
def save_recipe():
    return redirect('/dashboard')