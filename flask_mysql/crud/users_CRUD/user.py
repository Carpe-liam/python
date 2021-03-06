from flask.templating import render_template
from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['ID']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.upated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('dojo_users_schema').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE users.id = %(userID)s;"
        results = connectToMySQL('dojo_users_schema').query_db(query, data)
        user = cls(results[0])
        return user

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at)  VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
        return connectToMySQL('dojo_users_schema').query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE users.id = %(userID)s;"
        return connectToMySQL('dojo_users_schema').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE users.ID = %(userID)s;"
        return connectToMySQL('dojo_users_schema').query_db(query, data)