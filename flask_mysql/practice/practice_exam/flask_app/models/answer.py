from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import DATABASE, app

class Answer:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.owner = data['owner']
        self.question_id = data['question_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_answer(cls, data):
        query = """
        INSERT INTO answers (user_id, question_id, content)
        VALUES (  %(user_id)s, %(question_id)s,  %(content)s )   ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_question_answers(cls, data):
        query = """
        SELECT users.username AS owner, answers.* FROM answers
        LEFT JOIN users
        ON answers.user_id = users.id
        JOIN questions
        ON users.id = questions.user_id
        WHERE answers.question_id = %(id)s  ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        answers = []

        for answer in results:
            answers.append(cls(answer))
        return answers