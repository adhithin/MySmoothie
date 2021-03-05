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
        fruits = request.form.getlist('fruits')
        print(fruits)
        if 'Bananas' and 'Strawberries' in fruits:
            return render_template("bananas&strawberries.html")
        if 'Bananas' in fruits:
            return render_template("bananas.html")
        #for fruit in fruits:
        #if fruits == 'Bananas' and fruits == "Strawberries":
            #return render_template("bananas.html")
        #if fruits == 'Strawberries':
            #return render_template("home.html")
        #return render_template("selection.html")
    return render_template("selection.html")

@app.route('/browse-recipes', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html')



if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

