from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime 
import math
from flask_app import DATABASE

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.sender = data['sender']
        self.sender_id = data['sender_id']
        self.receiver = data['receiver']
        self.receiver_id = data['receiver_id']
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
    def get_user_messages(cls, data):
        query = """
        SELECT users.first_name AS sender, users2.first_name AS receiver, messages.* FROM users
        LEFT JOIN messages
        ON users.id = messages.sender_id
        LEFT JOIN users AS users2
        ON users2.id = messages.receiver_id
        WHERE users2.id = %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        messages = []
        
        for message in results:
            messages.append(cls(message))
        return messages

    @classmethod
    def post_message(cls, data):
        query = """
        INSERT INTO messages (sender_id, receiver_id, content)
        VALUES ( %(sender_id)s, %(receiver_id)s, %(content)s )
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = """
        DELETE FROM messages WHERE messages.id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)