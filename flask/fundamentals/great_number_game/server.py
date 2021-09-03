import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "wizard"

@app.route('/')
def home():
    session['random_number'] = random.randint(1,100)
    session['count'] = 1
    print("Magic Number is: " + str(session['random_number']))
    return render_template("index.html")

@app.route('/guess', methods=['POST', 'GET'])
def guess_check():
    session['choice'] = request.form['choice']
    if int(session['choice']) > session['random_number'] and int(session['count']) < 5:
        session['miss'] = "Nope, too high!"
        print("Count= "+ str(session['count']))
        #page should say too big
    elif int(session['choice']) < session['random_number'] and int(session['count']) < 5:
        session['miss'] = "Nope, too low!"
        print("Count= "+ str(session['count']))
    elif (int(session['count']) >= 5):
        return redirect('/lose')
    else:
        return redirect('/success')
    print("Got Post Info")
    session['count']+=1
    return redirect('/post')

@app.route('/post')
def post():
    print("Magic Number is: " + str(session['random_number']))
    return render_template("index.html")

@app.route('/lose')
def lose():
    session['miss'] ="Mmm... maybe next time? The Magic number was " + str(session['random_number']) + " the whole time!"
    print("Magic Number is: " + str(session['random_number']))
    return render_template("index.html")

@app.route('/success')
def success():
    session['miss'] = "Success! You win! The Magic number was " + str(session['random_number']) + " the whole time!"
    print("Magic Number is: " + str(session['random_number']))
    return render_template("index.html")

@app.route('/kill')
def end_page():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)