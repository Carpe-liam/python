from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.controllers import ninjas

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos=dojos)


@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id' : id
    }
    ninjas = Ninja.dojo_ninjas(data)
    return render_template("one_dojo.html", ninjas=ninjas)








@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form['name']
    }
    Dojo.new_dojo(data)
    return redirect('/dojos')