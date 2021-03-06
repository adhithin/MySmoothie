from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc

basedir = os.path.abspath(os.path.dirname(__file__))

# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#OMG SO IMPORTANT TO INCLUDE THIS ABOVE! Warnings up the wazoo if not here on a develoment server.

db = SQLAlchemy(app)

class Recipes(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    # not planning to delete scores, but still a good practice
    p_recipe = db.Column(unique=False, nullable=False)
    p_ingredients = db.Column(unique=False, nullable=False) # want score as int so we can sort by it easily.
    p_steps = db.Column(unique=False, nullable=False)

    def __init__(self, p_recipe, p_ingredients, p_steps):
        self.p_recipe = p_recipe
        self.p_ingredients = p_ingredients
        self.p_steps = p_steps

    def __repr__(self):
        return f"{self.p_recipe},{self.p_ingredients}, {self.p_steps}"

#must go after 'models'
db.create_all();