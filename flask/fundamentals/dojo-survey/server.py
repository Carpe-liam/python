from flask import Flask, render_template, redirect, request, session

app= Flask(__name__)
app.secret_key='wizard'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/return')
def return_response():
    return render_template('return.html')

if __name__=="__main__":
    app.run(debug=True)

