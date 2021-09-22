from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, username, email, password)
        VALUES (  %(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s  )
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one_username(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.username = %(username)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("Got by username")
        print(results)
        return cls(results[0])

    @classmethod
    def get_one_id(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.id = %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("Got by id")
        print(results)
        return cls(results[0])


    @staticmethod
    def validate_reg(user): # remember that the request form is the user
        errors = {}
        if len(user['first_name']) < 2:
            errors['first_name'] = 'Name should be at least 2 characters.'

        if len(user['last_name']) < 2:
            errors['last_name'] = 'Name should be at least 2 characters.'

        if len(user['username']) < 4:
            errors['username'] = 'Username should be at least 2 characters.'

        query = "SELECT * FROM users WHERE users.username = %(username)s;"
        results = connectToMySQL(DATABASE).query_db(query,user)
        if len(results) >= 1:
            errors['invalid_username'] = "Username already taken, please choose diffferent username"

        if len(user['password']) < 8 :
            errors['password'] = 'Password should be at least 8 characters.'

        if user['password'] != user['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match.'

        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,user)
        if len(results) >= 1:
            errors['email'] = "Email already registered, please login."

        if not EMAIL_REGEX.match(user['email']): 
            errors['invalid_email'] = "Invalid email address!"

        for category,message in errors.items():
            flash(message,category)
        return len(errors) == 0