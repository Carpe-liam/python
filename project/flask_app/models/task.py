from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app


class Task:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
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
        WHERE users.id = %(id)s 
        ORDER BY tasks.due_by, tasks.importance ASC;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        tasks = []
        for task in results:
            tasks.append(cls(task))
        return tasks


    @classmethod
    def get_incomplete_tasks(cls, data):
        query = """
        SELECT * FROM tasks
        LEFT JOIN users
        ON tasks.user_id = users.id
        WHERE users.id = %(id)s AND completed = 0 
        ORDER BY tasks.due_by, tasks.importance ASC;
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
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
    def get_task_num(cls, data):
        query = """
        SELECT tasks.*, COUNT(tasks.id) AS num_tasks FROM tasks
        LEFT JOIN users
        ON tasks.user_id = users.id
        WHERE tasks.due_by = "2021-09-23" AND tasks.completed = 0 AND tasks.user_id = %(user_id)s
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        print("*"*80)
        print(results)
        print("*"*80)
        return cls(results[0]) 

    @classmethod
    def create_task(cls, data):
        query = """
        INSERT INTO tasks (user_id, title, description, importance, due_by)
        VALUES (  %(user_id)s, %(title)s, %(description)s, %(importance)s, %(due_by)s );
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def edit_task(cls, data):
        query = """
        UPDATE tasks
        SET title = %(title)s, description = %(description)s, importance = %(importance)s, due_by = %(due_by)s
        WHERE tasks.id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def complete_task(cls, data):
        query = """
        UPDATE tasks
        SET completed = 1
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
        if task['due_by'] == "":
            errors['due_by'] = "Please enter assingment due-date"
        if task['importance'] == "":
            errors['importance'] = "Please select importance level"

        for category, message in errors.items():
            flash(message,category)
        return len(errors) == 0