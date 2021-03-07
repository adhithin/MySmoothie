import os
from flask import Flask, render_template, flash, redirect, url_for, session, logging
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
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
    p_ingredients = db.Column(db.String(10), unique=False, nullable=False) # want score as int so we can sort by it easily.
    p_steps = db.Column(db.String(10), unique=False, nullable=False)

    def __init__(self, p_recipe, p_ingredients, p_steps):
        self.p_recipe = p_recipe
        self.p_ingredients = p_ingredients
        self.p_steps = p_steps

    def __repr__(self):
        return f"{self.p_recipe},{self.p_ingredients}, {self.p_steps}"

#must go after 'models'
db.create_all();

@app.route('/', methods=['GET', 'POST'])
def home():
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
    return render_template("selection.html")

@app.route('/browse-recipes', methods=['GET', 'POST'])
def browse():
    return render_template('browse.html')

@app.route('/add-recipes', methods=['GET', 'POST'])
def addrecipes():
    Recipe = 'nothing'

    if request.method == 'POST':
        recipe = request.form['recipe']
        ingredients = request.form.getlist('ingredients')
        steps = request.form['steps']

        new_recipe = Recipe(recipe, ingredients, steps)
        db.session.add(new_recipe)
        db.session.commit()

        listRecipes = Recipes.query.filter_by(p_recipe=recipe).order_by('p_recipe').all()
        listRecipes = []

        for listRecipe in listRecipes:
            recipe_dict = {'recipe':listRecipe.p_recipe, 'ingredients':listRecipe.p_steps}
            listRecipes.append(recipe_dict)

    return render_template("addrecipe.html")

@app.route('/get-your-smoothie/bananas', methods=['GET', 'POST'])
def bananas():
    return render_template("bananas.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='8034', host='127.0.0.1')

