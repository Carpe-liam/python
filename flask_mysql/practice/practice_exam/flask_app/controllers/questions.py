from flask_app import app
from flask import flash, session, render_template, redirect, request
from flask_app.models.user import User
from flask_app.controllers import users, answers
from flask_app.models.question import Question
from flask_app.models.answer import Answer

@app.route('/new_question')
def display_new_form():
    data = {
        'id':session['user_id']
    }
    user = User.get_one_id(data)
    return render_template("new_question.html", user=user)


@app.route('/create_question', methods=["POST"])
def create_question():
    if 'user_id' not in session: 
        return redirect('/')
    if not Question.validate_question(request.form):
        return redirect('/new_question')
    data = {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "user_id" : session['user_id']
    }
    Question.create_question(data)
    return redirect('/userpage')


@app.route("/view_question/<int:id>")
def view_question(id):
    if 'user_id' not in session: 
        return redirect('/')
    data = {
        "id" : id
    }
    question = Question.get_single_question(data)
    answers = Answer.get_question_answers(data)
    print(answers)
    user_data = {
        "id" : session["user_id"]
    }
    user = User.get_one_id(user_data)
    return render_template("view_question.html", user=user, question=question, answers=answers)