from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re #EMAIL REGEX IMPORT
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM emails;
        """
        results = connectToMySQL('email_db').query_db(query)
        emails = []
        for email in results:
            emails.append(cls(email))
        return emails

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO emails (email)
        VALUES (  %(email)s  )
        """
        results = connectToMySQL('email_db').query_db(query, data)
        return results

    @classmethod
    def delete(cls,data):
        query = """
        DELETE FROM emails
        WHERE id = %(id)s ;
        """
        return connectToMySQL('email_db').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM emails
        WHERE id = %(id)s ;
        """
        results = connectToMySQL('email_db').query_db(query, data)
        email_one = cls(results[0])
        return email_one


    @staticmethod
    def validate_email(email_one): #request form
        is_valid = True
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('email_db').query_db(query,email_one)
        if len(results) >= 1:
            flash("Email already taken.")
            is_valid=False
        if not EMAIL_REGEX.match(email_one['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

