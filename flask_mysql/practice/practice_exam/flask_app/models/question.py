from werkzeug.utils import validate_arguments
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE, app

class Question:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.description = data['description']
        self.answered = data['answered']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_question(cls, data):
        query = """
        INSERT INTO questions (user_id, title, description, answered)
        VALUES (  %(user_id)s, %(title)s, %(description)s, "No"  ) ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def update_question(cls, data):
        qeury = """
        
        """


    @classmethod
    def get_single_question(cls,data):
        query = """
        SELECT * FROM questions
        LEFT JOIN users
        ON questions.user_id = users.id
        WHERE questions.id = %(id)s   ;
        """
        print(query)
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])


    @classmethod
    def get_all_questions(cls):
        query = """
        SELECT questions.*, users.username FROM questions 
        LEFT JOIN users
        ON questions.user_id = users.id
        ORDER BY questions.created_at DESC ;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        return results


    @staticmethod
    def validate_question(question): #request form is user
        errors = {}
        if len(question['title']) < 20:
            errors['title'] = 'Questions must be at least 20 characters.'

        for category,message in errors.items():
            flash(message,category)
        return len(errors) == 0