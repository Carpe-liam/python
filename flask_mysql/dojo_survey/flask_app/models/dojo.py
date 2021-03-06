from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_one(cls, data):
        query = """
        SELECT * FROM dojos 
        WHERE id = %(id)s ;
        """
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        survey = cls(results[0])
        return survey

    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO dojos (name, location, language, comment)
        VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s );
        """
        results = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return results

    @staticmethod
    def validate_survey(survey): #survey IS request.form
        errors = {}
        if len(survey['name']) < 3:
            errors['name'] = 'Name should be at least 3 characters.'
            #flash('Name should be at least 3 characters.', name)
            #is_valid = False
        if survey['location'] not in ['London', 'Athens', 'Dallas', 'Auckland', 'Online']:
            errors['location'] = 'Location should one of the following options.'
            #flash('Location should one of the following options.', location)
            #is_valid = False
        if survey['language'] not in ['Java', 'Python', 'MERN', 'C#', 'Ruby']:
            errors['language'] = 'Language should one of the following options.'
            #flash('Language should one of the following options.', language)
            #is_valid = False
        for category,message in errors.items():
            flash(message,category)
        return len(errors) == 0