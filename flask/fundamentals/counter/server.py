from flask import Flask, render_template, request, redirect, session
from flask.templating import render_template_string

app = Flask(__name__)
app.secret_key= 'secret_1234_key'

@app.route('/')
def greeting():
    if 'visits' in session:
        session['visits']+=1
    else:
        session['visits'] =1
    return render_template("index.html")


@app.route('/users')
def count_vists():
    session['visits']+=1
    print("Got Post Info")
    return redirect('/')


@app.route('/destroy_session')
def end_page():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)