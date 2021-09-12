from flask import Flask
app = Flask(__name__)
app.secret_key = "wizard"

DATABASE = 'users_login_schema'