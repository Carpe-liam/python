from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import DATABASE, app

class User:
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_user(cls, data):
        query = """
        INSERT INTO users (username,email, password)
        VALUES (  %(username)s, %(email)s, %(password)s  ) ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_one_id(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.id = %(id)s ;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        if not result: 
            return False
        return cls(result[0])


    @classmethod
    def get_one_email(cls, data):
        query = """
        SELECT * FROM users
        WHERE users.email = %(email)s ;
        """
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])


    @staticmethod
    def validate_user(user): #request form is user
        errors = {}
        if len(user['username']) < 5:
            errors['username'] = 'Userame should be at least 5 characters.'

        if len(user['password']) < 8 :
            errors['password'] = 'Password should be at least 8 characters.'

        if user['password'] != user['password_check']:
            errors['password_check'] = 'Passwords do not match'

        query = "SELECT * FROM users WHERE users.email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,user)
        if len(results) >= 1:
            errors['email'] = "Email already taken."

        if not EMAIL_REGEX.match(user['email']): 
            errors['invalid_email'] = "Invalid email address!"

        for category,message in errors.items():
            flash(message,category)
        return len(errors) == 0