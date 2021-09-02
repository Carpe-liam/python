from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/<string:user>')
def greeting(user):
    return f"Hi {user}!"

@app.route('/repeat/<int:num>/<string:thing>')
def repeat(num, thing):
    return f"{thing * num} "

if __name__ == '__main__':
    app.run(debug=True)