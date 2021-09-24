from flask import flash, session, render_template, redirect, request
from flask_app.controllers import tasks, users
from flask_app.models.user import User
from flask_app.models.task import Task
from flask_app.models.note import Note
from flask_app import app

@app.route("/create_note", methods=["POST"])
def create_note():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "content" : request.form['content'],
        "id" : request.form["id"]
    }
    Note.create_note(data)
    return redirect(f"/view/{request.form['id']}")