from flask import Flask, render_template, redirect, request, session
import random

app= Flask(__name__)
app.secret_key='wizard'


@app.route('/')
def home():
    if "my_money" not in session:
        session['my_money']=0
        session['last_transaction'] = "<p> Oh no! You haven't gone for gold! </p>"
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def get_my_money():
    session['location'] = request.form['location']
    if session['location'] == 'farm':
        session['my_money']+= random.randint(10,20) 
        session['last_transaction'] += "<p class='text-success'> You got " + str(session['my_money']) + " gold!</p>"
    elif session['location'] == 'house':
        session['my_money']+= random.randint(5,10) 
        session['last_transaction'] += "<p class='text-success'> You got " + str(session['my_money']) + " gold!</p>"
    elif session['location'] == 'cave':
        session['my_money']+= random.randint(2, 5) 
        session['last_transaction'] += "<p class='text-success'> You got " + str(session['my_money']) + " gold!</p>"
    else:
        session['my_money']+= random.randint(-50, 50) 
        session['last_transaction'] += "<p class='text-danger'> You got " + str(session['my_money']) + " gold!</p>"
    
    
    
    print(request.form)
    print("this is my money: " + str(session['my_money']))




    return redirect('/')

@app.route('/kill')
def kill():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)


