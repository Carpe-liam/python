from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app


class Task:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.importance = data['importance']
        self.completed = data['completed']
        self.due_by = data['due_by']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_user_tasks(cls, data):
        query = """
        SELECT * FROM tasks
        LEFT JOIN users
        ON tasks.user_id = users.id
        WHERE users.id = %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        tasks = []
        for task in results:
            tasks.append(cls(task))
        return tasks


    @classmethod
    def get_one_task(cls, data):
        query = """
        SELECT * FROM tasks
        WHERE tasks.id = %(id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        task = cls(results[0])
        return task


    @classmethod
    def create_task(cls, data):
        query = """
        INSERT INTO tasks (user_id, title, description, importance, completed, due_by)
        VALUES (  %(user_id)s, %(title)s, %(description)s, %(importance)s, %(completed)s, %(due_by)s );
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def edit_task(cls, data):
        query = """
        UPDATE tasks
        SET title = %(title)s, descriptions = %(description)s, importance = %(importance)s, completed = %(completed)s, due_by = %(due_by)s
        WHERE tasks.id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete_task(cls, data):
        query = """
        DELETE FROM tasks
        WHERE tasks.id = %(id)s
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_task(task):
        errors = {}
        if len(task['title']) <3:
            errors['title'] = "Title should be at least 3 characters"
        if len(task['due_date']) <3:
            errors['due_date'] = "Please enter assingment due-date"
        if len(task['importance']) <3:
            errors['importance'] = "Please select importance level"

        for category, message in errors.items():
            flash(message,category)
        return len(errors) == 0