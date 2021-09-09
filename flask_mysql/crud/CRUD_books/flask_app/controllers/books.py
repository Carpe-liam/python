from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template("books.html", books = books)


@app.route('/books/<int:id>')
def book_profile(id):
    data = {
        'id' : id
    }
    book = Book.get_one(data)
    authors = Author.get_all()
    return render_template("book_faves.html", book = book, authors=authors)


@app.route('/write_book', methods=["POST"])
def write_book():
    data = {
        "title" : request.form["title"],
        "num_of_pages" : request.form["num_of_pages"]
    }
    Book.write_book(data)
    return redirect('/books')

@app.route('/author_fave', methods=["POST"])
def auth_fave():
    data = {
        'book_id' : request.form['book_id'],
        'author_id' : request.form['author_id']
    }
    Book.auth_fave(data)
    return redirect('/books')
