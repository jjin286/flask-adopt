"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import URL, Optional, InputRequired

class AddPetForm(FlaskForm):
    """Form for adding new pet"""

    name = StringField("Pet name",validators=[InputRequired()])
    species = SelectField('Species',
        choices=[
        ('cat','Cat'),
        ('dog', 'Dog'),
        ('porcupine', 'Porcupine')],validators=[InputRequired()])
    photo_url = StringField("Photo URL",validators=[URL(),Optional()])
    age = SelectField('Age',
        choices=[
            ('baby','Baby'),
            ('young', 'Young'),
            ('adult', 'Adult'),
            ('senior', 'Senior')],validators=[InputRequired()])
    notes = StringField("Notes",validators=[Optional()])

class EditPetForm(FlaskForm):
    """ Form for editing a pet """

    photo_url = StringField("Photo URL",validators=[URL(),Optional()])
    notes = StringField("Notes",validators=[Optional()])
    available = BooleanField("Availability",default="checked",validators=[InputRequired()])