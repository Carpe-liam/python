from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app

class Note:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_notes(cls, data):
        query = """
        SELECT * FROM notes
        LEFT JOIN tasks
        ON notes.task_id = tasks.id
        WHERE tasks.id = %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        notes = []
        for note in results:
            notes.append(cls(note))
        return notes
    
    