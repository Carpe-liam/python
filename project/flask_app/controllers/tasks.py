from flask import flash, session, render_template, redirect, request
from flask_app.controllers import users, notes
from flask_app.models.user import User
from flask_app.models.note import Note
from flask_app.models.task import Task
from flask_app import app

@app.route("/new_task")
def new_task():
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" : session['user_id']
    }
    user = User.get_one_id(data)
    tasks = Task.get_user_tasks(data)
    return render_template("new_task.html", user=user, tasks=tasks)


@app.route("/view/<int:id>")
def view_task(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    task = Task.get_one_task(data)
    notes = Note.get_all_notes(data) 
    userID = {
        "id" : session['user_id']
    }
    user = User.get_one_id(userID)
    return render_template("show_task.html", task=task, user=user, notes=notes)


@app.route("/edit/<int:id>")
def edit_task(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    task = Task.get_one_task(data)
    notes = Note.get_all_notes(data)
    userID = {
        "id" : session['user_id']
    }
    user = User.get_one_id(userID)
    return render_template("edit_task.html", task=task, user=user, notes=notes)


@app.route("/complete/<int:id>")
def complete_task(id):
    if "user_id" not in session:
        return redirect("/")
    data = {
        "id":id
    }
    Task.complete_task(data)
    return redirect("/dashboard")


@app.route("/create_task", methods=["POST"])
def create_task():
    if 'user_id' not in session:
        return redirect("/")
    if not Task.validate_task(request.form):
        return redirect("/new_task")
    data = {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "due_by" : request.form['due_by'],
        "importance" : request.form['importance'],
        "user_id" : request.form['user_id']
    }
    Task.create_task(data)
    return redirect("/dashboard")


@app.route("/update_task", methods=["POST"])
def update_task():
    if 'user_id' not in session:
        return redirect("/")
    if not Task.validate_task(request.form):
        return redirect(f"/edit/{request.form['id']}")
    data = {
        "title" : request.form['title'],
        "description" : request.form['description'],
        "due_by" : request.form['due_by'],
        "importance" : request.form['importance'],
        "user_id" : request.form['user_id'],
        "id" : request.form['id']
    }
    Task.edit_task(data)
    return redirect("/dashboard")


@app.route("/delete/<int:id>")
def delete_task(id):
    if 'user_id' not in session:
        return redirect("/")
    data = {
        "id" :id
    }
    Task.delete_task(data)
    return redirect("/dashboard")