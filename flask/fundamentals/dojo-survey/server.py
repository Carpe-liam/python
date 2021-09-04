from flask import Flask, render_template, redirect, request, session

app= Flask(__name__)
app.secret_key='wizard'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/return', methods=["POST"])
def return_response():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    if 'agreement' not in request.form:
        session['agreement'] = "No"
    else:
        session['agreement'] = "Yes, I owe you lunch now"
        if 'lunch' not in request.form:
            session['lunch'] = "No"
        else:
            session['lunch'] = "Yes"
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('result.html')

@app.route('/kill')
def kill():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

