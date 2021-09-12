from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app.controllers import dojos


@app.route('/ninjas')
def ninja():
    dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos=dojos)

@app.route('/ninjas/roster')
def roster():
    ninjas = Ninja.get_all()
    return render_template("roster.html", ninjas = ninjas)

@app.route('/create', methods=["POST"])
def create():
    data = {
        'dojo_id' : request.form['dojo_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    print(data)
    Ninja.create(data)
    return redirect('/dojos')

