from flask_app import app, DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.name = data['name']
        self.ingredients = data['ingredients']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made_on = data['date_made_on']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def save(cls,data):
        