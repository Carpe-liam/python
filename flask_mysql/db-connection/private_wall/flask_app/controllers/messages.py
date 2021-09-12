from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.message import Message
from flask_app.controllers import users

@app.route('/create_message', methods=["POST"])
def create_message():
    data = {
        'sender_id' : request.form['sender_id'],
        'receiver_id' : request.form['receiver_id'],
        'content' : request.form['content']
    }
    Message.post_message(data)
    return redirect('/welcome')

@app.route('/destroy/message/<int:id>')
def delete_message(id):
    data = {
        'id' : id
    }
    Message.destroy(data)
    return redirect('/welcome') 