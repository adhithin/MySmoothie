import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
import cgi, cgitb
# Create instance of FieldStorage

form = cgi.FieldStorage()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/get-your-smoothie', methods=['GET', 'POST'])
def find():
    fruits = 'nothing'
    if request.method == 'POST':
        fruit1 = request.form['fruit1']
        print("here's some things you can do with apples")

    for fruit in fruits:
        if form.getvalue('Apple'):
            print("The email address is '" + email + "'")
            return redirect('/')
        else:
            fruit1 = "OFF"
            return render_template("selection.html")
        if form.getvalue('Banana'):
            fruit2 = "ON"
            return render_template("fruit1.html")
        else:
            fruit2 = "OFF"
            return render_template("selection.html")



    return render_template("selection.html")



if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

