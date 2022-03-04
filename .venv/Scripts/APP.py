import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,
                                                                    '../TekSystems/tek-robinson-python2/.venv/Scripts/data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


###################################
class Puppy(db.Model):

    __tablename__ = 'puppies'
    id(db.Column(db.Integer, primary_key=True))
    name: str = db.Column(db.Text)
    age = db.Column(db.Integer)
    owners = db.relationship('Owner', backref='puppy', uselist=false)


def __init__(self, name, age):
    self.name = name
    self.age = age


def __repr__(self):
    if self.owner:
        return f'Puppy name is{self.name} and owner is {self.owner.name}'
    else:
        return f'Puppy name: {self.name} and no owner assigned yet!'
    return f"Puppy {self.name} is {self.age} year/s old"

class Owner(db.Model)

        __tablename__ = "Owners"

        id(db.Column(db.Integer, primary_key=True))
        name = db.Column(db.Text)
        puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,name, puppy_id):
        self.name=name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"