import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from bs4 import BeautifulSoup
import smtplib
import time


# Create instance of FieldStorage

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a development server.

db = SQLAlchemy(app)

class Recipes(db.Model):
    __tablename__ = 'Recipe'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_recipe = db.Column(db.String(10), unique=False, nullable=False)
    p_steps = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, p_recipe, p_steps):
        self.p_recipe = p_recipe
        self.p_steps = p_steps

    def __repr__(self):
        return f"{self.p_recipe}, {self.p_steps}"

#must go after 'models'
db.create_all();




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']
        def send_email():
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('adhithi.nmurthy07@gmail.com', 'yavesbrwlogwvuaa')

            subject = 'Hello from MySmoothie!'

            body = 'Check out the website to learn about Bananas: https://en.wikipedia.org/wiki/Banana'

            msg = f"Subject: {subject}\n\n{body}"

            server.sendmail(
                'adhithi.nmurthy07@gmail.com',
                email,
                msg

            )

            server.quit()

        send_email()

    return render_template('home.html')

@app.route('/get-your-smoothie', methods=['GET', 'POST'])
def find():
    fruits = 'nothing'
    if request.method == 'POST':
        fruits = request.form.getlist('fruits')
        print(fruits)
        if 'Bananas' and 'Strawberries' and 'Blueberries' in fruits:
            return render_template("bananas&strawberries.html")
        if 'Bananas' and 'Strawberries' in fruits:
            return render_template("bananas&strawberries.html")
        if 'Bananas' in fruits:
            return render_template("bananas.html")
        if 'Strawberries' in fruits:
            return render_template("home.html")
        if 'Blueberries' in fruits:
            return render_template("home.html")
        if 'Apples' in fruits:
            return render_template("home.html")
    return render_template("selection.html")

@app.route('/browse-recipes', methods=['GET', 'POST'])
def browse():
    Recipes = 'nothing'

    if request.method == 'POST':
        recipe = request.form['recipe']
        steps = request.form['steps']

    return render_template('browse.html')

@app.route('/add-recipes', methods=['GET', 'POST'])
def addrecipes():
    if request.method == 'POST':
        recipe = request.form['recipe']
        steps = request.form['steps']

        #the code below confirmed I had the proper data. Now to add it to the db.
        print(recipe)
        print(steps)

        new_recipe = Recipes(recipe, steps)
        db.session.add(new_recipe)
        db.session.commit()

    #query the db for the ratings:
    recipe_book = Recipes.query.order_by(desc('p_recipe')).all()
    recipeList = []

    for listrecipe in recipe_book:
        recipe_dict = {'recipe':recipe.p_name, 'steps':recipe.p_steps}
        recipeList.append(recipe_dict)

    return render_template('addrecipe.html', recipeList = recipeList)




if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

