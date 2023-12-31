"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
import requests
db = SQLAlchemy()
import os
from random import sample


# this HAS to be imported if not in app.py
from dotenv import load_dotenv
load_dotenv()

API_SECRET_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']
API_TOKEN = os.environ['API_TOKEN']




def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for Pet"""

    __tablename__ = "pets"

    id = db.Column(
        db.Integer,
        primary_key=True)

    name = db.Column(
        db.Text,
        nullable=False)

    species = db.Column(
        db.Text,
        nullable=False)

    photo_url = db.Column(
        db.Text,
        nullable=False)

    age = db.Column(
        db.Text,
        nullable=False)

    notes = db.Column(
        db.Text,
        nullable=False)

    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True)

    __table_args__= dict(CheckConstraint(age in ['baby','young','adult','senior']))

    @classmethod
    def get_random_PetFinder_pet(cls):
        ''' Requests PetFinder API to get a list of pets,
            then randomly selects one '''
        print("WE MADE IT")
        pets = requests.get('https://api.petfinder.com/v2/animals?limit=100',
                            headers={"Authorization": f"Bearer {API_TOKEN}"}).json()
        # print("type", type(pets['animals']))
        print("Pet", type(pets))
        random_pet = sample(pets['animals'], 1)
        age = random_pet[0]['age']
        name = random_pet[0]['name']
        species = random_pet[0]['species']
        try:
            photo_url = random_pet[0]['photos'][0]
        except:
            photo_url = ('https://i.pinimg.com/736x/92/dd/1c/92dd1cd7871f642eaf69d4928d069c78.jpg')

        pet = {"age": age,"name": name,"species": species, 'photo_url':photo_url}

        return pet


