from flask_app import app
from flask import flash, session, render_template, redirect, request
from flask_app.models.user import User
from flask_app.models.answer import Answer
from flask_app.controllers import users, questions


@app.route("/submit_answer", methods=["POST"])
def new_answer():
    if 'user_id' not in session: 
        return redirect('/')
    data = {
        "user_id" : request.form["user_id"],
        "question_id" : request.form["question_id"],
        "content" : request.form["content"]
    }
    answer = Answer.create_answer(data)
    print(answer)
    return redirect("/userpage")



