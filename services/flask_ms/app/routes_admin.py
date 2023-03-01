from flask import Blueprint, redirect, request, jsonify, render_template, url_for
from .models import db, Person, Vehicle, Official, Infraction
from .forms import PersonForm, VehicleForm, OfficialForm

admin = Blueprint('admin', __name__, url_prefix='/admin')

# Show the list of person
@admin.route('/person', methods=['GET'])
def person_list():
    # Retrieve all person from the database
    person = Person.query.all()
    # Render the person.html template with the retrieved person
    return render_template('admin/person_list.html', people=person)

# Show the form to create a new person
@admin.route('/person/new', methods=['GET', 'POST'])
def new_person():
    form = PersonForm()
    if form.validate_on_submit():
        # Create a new person object with data from the form
        person = Person(
            name=form.name.data,
            email=form.email.data
        )
        # Add the new person to the database
        db.session.add(person)
        db.session.commit()
        # Redirect to the list of people
        return redirect(url_for('admin.person_list'))
    return render_template('admin/person_form.html', form=form)

# Show the form to edit an existing person
@admin.route('/person/<int:id>/edit', methods=['GET', 'POST'])
def edit_person(id):
    # Retrieve the person with the given ID or return a 404 error if it does not exist
    person = Person.query.get_or_404(id)
    # Create a new PersonForm with the retrieved person's data
    form = PersonForm(obj=person)
    # If the form was submitted and is valid, update the retrieved person's data in the database
    if form.validate_on_submit():
        person.name = form.name.data
        person.email = form.email.data
        db.session.commit()
        return redirect(url_for('admin.person_list'))
    # Render the person.html template with the form and the retrieved person
    return render_template('admin/person_form.html', form=form, person=person)

# delete a person
@admin.route('/person/<int:id>/delete', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get_or_404(id)
    db.session.delete(person)
    db.session.commit()
    return redirect(url_for('admin.person_list'))

# Show the list of vehicles
@admin.route('/vehicles', methods=['GET'])
def vehicle_list():
    # Retrieve all vehicles from the database
    vehicles = Vehicle.query.all()
    # Render the vehicle.html template with the retrieved vehicles
    return render_template('admin/vehicle_list.html', vehicles=vehicles)

# Show the form to create a new vehicle
@admin.route('/vehicle/new', methods=['GET', 'POST'])
def new_vehicle():
    form = VehicleForm()
    people = Person.query.all() 
    form.owner.choices = [(p.id, p.name) for p in people]
    if form.validate_on_submit():
        owner_id = form.owner.data
        owner = Person.query.filter_by(id=owner_id).first()
        if owner is None:
            return redirect(url_for('admin.vehicle_list'))
        vehicle = Vehicle(
            license_plate=form.license_plate.data,
            brand=form.brand.data,
            color=form.color.data,
            person_id=owner.id
        )
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for('admin.vehicle_list'))
    return render_template('admin/vehicle_form.html', form=form)

# Show the form to edit an existing vehicle
@admin.route('/vehicle/<int:id>/edit', methods=['GET', 'POST'])
def edit_vehicle(id):
    # Retrieve the vehicle with the given ID or return a 404 error if it does not exist
    vehicle = Vehicle.query.get_or_404(id)
    # Create a new VehicleForm with the retrieved vehicle's data
    form = VehicleForm(obj=vehicle)
    # Add choices to the owner field in the form
    form.owner.choices = [(p.id, p.name) for p in Person.query.all()]
    # If the form was submitted and is valid, update the retrieved vehicle's data in the database
    if form.validate_on_submit():
        owner_id = form.owner.data
        owner = Person.query.get(owner_id)
        if owner is None:
            return redirect(url_for('admin.vehicle_list'))
        vehicle.license_plate = form.license_plate.data
        vehicle.brand = form.brand.data
        vehicle.color = form.color.data
        vehicle.person_id = owner.id
        db.session.commit()
        return redirect(url_for('admin.vehicle_list'))
    people = Person.query.all()
    # Render the vehicle_form.html.html template with the form and the retrieved vehicle
    return render_template('admin/vehicle_form.html', form=form, vehicle=vehicle, people=people)

# delete vehicle
@admin.route('/vehicle/<int:id>/delete', methods=['DELETE'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({'message': 'Vehicle deleted successfully.'})

# Show the list of officials
@admin.route('/officials', methods=['GET'])
def official_list():
    # Retrieve all officials from the database
    officials = Official.query.all()
    # Render the official.html template with the retrieved officials
    return render_template('admin/official_list.html', officials=officials)

# Show the form to create a new official
@admin.route('/official/new', methods=['GET', 'POST'])
def new_official():
    form = OfficialForm()
    if form.validate_on_submit():
        official = Official(
            name=form.name.data,
            identification_number=form.identification_number.data
        )
        db.session.add(official)
        db.session.commit()
        return redirect(url_for('admin.official_list'))
    return render_template('admin/official_form.html', form=form)

# Show the form to edit an existing official
@admin.route('/official/<int:id>/edit', methods=['GET', 'POST'])
def edit_official(id):
    # Retrieve the official with the given ID or return a 404 error if it does not exist
    official = Official.query.get_or_404(id)
    # Create a new OfficialForm with the retrieved official's data
    form = OfficialForm(obj=official)
    # If the form was submitted and is valid, update the retrieved official's data in the database
    if form.validate_on_submit():
        official.name = form.name.data
        official.identification_number = form.identification_number.data
        db.session.commit()
        return redirect(url_for('admin.official_list'))
    # Render the official_form.html template with the form and the retrieved official
    return render_template('admin/official_form.html', form=form, official=official)

# edelete official
@admin.route('/official/<int:id>/delete', methods=['DELETE'])
def delete_official(id):
    official = Official.query.get_or_404(id)
    db.session.delete(official)
    db.session.commit()
    return jsonify({'message': 'Official deleted successfully.'})