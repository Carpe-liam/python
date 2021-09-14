from flask import Flask
app = Flask(__name__)
app.secret_key = "wizard"

DATABASE = '{{enter database here}}'