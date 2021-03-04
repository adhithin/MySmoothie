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
    if form.getvalue('Apple'):
        fruit1 = "ON"
        print("amazing")
    else:
        fruit1 = "OFF"
    if form.getvalue('Banana'):
        fruit2 = "ON"
    else:
        fruit2 = "OFF"
    return render_template('selection.html')



if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

