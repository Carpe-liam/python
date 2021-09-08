from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo


@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)

@app.route('/ninjas')
def create_ninja():
    return render_template("ninjas.html")

@app.route('/create_dojo')
def create_dojo():
    return render_template("one_dojo.html")