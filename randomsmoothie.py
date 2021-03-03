import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def selection():
    return render_template('home.html')


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

