from flask.templating import render_template
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query,data)
        dojo = cls(results[0])
        return dojo

    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW() );"
        return connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query, data)

