from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.author import Author
from flask_app.models.book import Book
from flask_app.controllers import books

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template("authors.html", authors = authors)

@app.route('/authors/<int:id>')
def profile(id):
    data ={
        'id' : id
    }
    books = Book.get_all()
    author = Author.get_one(data)
    return render_template("author_faves.html", author=author, books=books)

@app.route('/new_auth', methods=["POST"])
def new_auth():
    data = {
        'name' : request.form['name']
    }
    Author.new_auth(data)
    return redirect('/authors')

@app.route('/book_fave', methods=["POST"])
def book_fave():
    data = {
        'book_id' : request.form['book_id'],
        'author_id' : request.form['author_id']
    }
    Author.book_fave(data)
    return redirect('/authors')