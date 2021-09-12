from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Survey

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/validate', methods=["POST"])
def validate():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    survey_id = Survey.create(request.form)
    session['survey_id'] = survey_id
    return redirect('/result')

@app.route('/result')
def show_survey():
    data = {
        'id' : session['survey_id']
    }
    survey = Survey.get_one(data)
    return render_template('result.html', survey=survey)