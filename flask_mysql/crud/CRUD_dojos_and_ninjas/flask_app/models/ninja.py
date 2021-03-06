from flask.templating import render_template
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query)
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def dojo_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query, data)
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) VALUES ( %(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW() );"
        return connectToMySQL('dojos-and-ninjas-dojo_schema').query_db(query, data)