from flask_app import app
from flask_app.models.email import Email
from flask import render_template, redirect, request, session, flash

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/validate', methods=["POST"])
def validate_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    email_id = Email.create(request.form)
    session['email_id'] = email_id
    return redirect('/success')

@app.route('/success')
def success():
    data = {
        'id' : session['email_id']
    }
    email = Email.get_one(data)
    all_emails = Email.get_all()
    return render_template("success.html", email = email, all_emails= all_emails)

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id' : id
    }
    Email.delete(data)
    return redirect('/success')