import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def selection():
    fruits = 'nothing'

    if request.method == 'POST':
        banana = request.form['banana']

        if banana == 1:
            print("yay")

        for b in fruits:
            print("yay")

    return render_template('selection.html')


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

