from flask.globals import request
from flask.templating import render_template
from flask_app.config.mysqlconnection import connectToMySQL
#from flask_app.models.book import Book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('dojo_books-schema').query_db(query)
        authors = []

        for author in results:
            authors.append(cls(author))
        return authors

    @classmethod
    def new_auth(cls, data):
        query= """
        INSERT INTO authors (name, created_at, updated_at)
        VALUES ( %(name)s, NOW(), NOW() );
        """
        return connectToMySQL('dojo_books-schema').query_db(query, data)


    @classmethod
    def book_fave(cls,data):
        query = """
        INSERT INTO favorites ( favorites.book_id, favorites.author_id)
        VALUES ( %(book_id)s, %(author_id)s );
        """
        return connectToMySQL('dojo_books-schema').query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM authors 
        LEFT JOIN favorites 
        ON authors.id = favorites.author_id 
        LEFT JOIN books 
        ON favorites.book_id = books.id
        WHERE authors.id = %(id)s;
        """
        results = connectToMySQL('dojo_books-schema').query_db(query,data)
        
        author = cls(results[0])
        author.books = []
        for book in results:
            bookdata = {
                'id' : book['books.id'],
                'title' : book['title'],
                'num_of_pages' : book['num_of_pages'],
                'created_at' : book['books.created_at'],
                'updated_at' : book['books.updated_at']
            }
            author.books.append(bookdata)
        
        return author