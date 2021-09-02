from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome!"

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def index(num=3, color='black'):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)