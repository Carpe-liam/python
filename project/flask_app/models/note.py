from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app
from datetime import datetime
import math

class Note:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        if delta.days > 0:
            return f"{delta.days} days ago"
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f"{math.floor(math.floor(delta.total_seconds() / 60)/60)} hours ago"
        elif delta.total_seconds() >= 60:
            return f"{math.floor(delta.total_seconds() / 60)} minutes ago"
        else:
            return f"{math.floor(delta.total_seconds())} seconds ago"

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


    @classmethod
    def create_note(cls, data):
        query = """
        INSERT INTO notes (task_id, content)
        VALUES (  %(id)s, %(content)s  ) 
        """
        return connectToMySQL(DATABASE).query_db(query, data)

