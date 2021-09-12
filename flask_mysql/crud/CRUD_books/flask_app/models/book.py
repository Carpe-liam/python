from flask.globals import request
from flask.templating import render_template
from flask_app.config.mysqlconnection import connectToMySQL
#from flask_app.models.author import Author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('dojo_books-schema').query_db(query)
        books = []

        for book in results:
            books.append(cls(book))
        return books

    @classmethod
    def write_book(cls, data):
        query = """
        INSERT INTO books (title, num_of_pages, created_at, updated_at)
        VALUES ( %(title)s, %(num_of_pages)s, NOW(), NOW() );
        """
        return connectToMySQL('dojo_books-schema').query_db(query, data)


    @classmethod
    def auth_fave(cls,data):
        query = """
        INSERT INTO favorites ( favorites.book_id, favorites.author_id)
        VALUES ( %(book_id)s, %(author_id)s );
        """
        return connectToMySQL('dojo_books-schema').query_db(query, data)


    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * 
        FROM books 
        LEFT JOIN favorites 
        ON books.id = favorites.book_id 
        LEFT JOIN authors 
        ON favorites.author_id = authors.id
        WHERE books.id = %(id)s;
        """
        results = connectToMySQL('dojo_books-schema').query_db(query,data)

        book = cls(results[0])
        book.authors = []
        for author in results:
            authordata = {
                'id' : author['authors.id'],
                'name' : author['name'],
                'created_at' : author['authors.created_at'],
                'updated_at' : author['authors.updated_at']
            }
            book.authors.append(authordata)
        return book