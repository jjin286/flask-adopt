"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def show_pets():
    """Shows a list of pets"""

    pets = Pet.query.all()
    random_pet = Pet.get_random_PetFinder_pet()

    return render_template('pet_list.html', pets=pets, random_pet=random_pet)


@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """Show new pet form and handle pet submit"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    else:
        return render_template("pet_add_form.html", form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_info_and_edit_form(pet_id):
    """Show pet info and edit form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.commit()

        return redirect(f"/{pet_id}")
    else:
        return render_template('pet_info.html', pet=pet, form=form)