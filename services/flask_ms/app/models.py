from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(
        db.Integer, primary_key=True)
    name = db.Column(
        db.String(100), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False)
    vehicles = db.relationship('Vehicle', backref='person', lazy=True)

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(
        db.Integer, primary_key=True)
    license_plate = db.Column(
        db.String(10), nullable=False)
    brand = db.Column(
        db.String(50), nullable=False)
    color = db.Column(
        db.String(50), nullable=False)
    person_id = db.Column(
        db.Integer, db.ForeignKey('persons.id'),nullable=False)
    infractions = db.relationship('Infraction', backref='vehicle', lazy=True)

class Official(db.Model):
    __tablename__ = 'officials'
    id = db.Column(
        db.Integer, primary_key=True)
    name = db.Column(
        db.String(100), nullable=False)
    identification_number = db.Column(
        db.String(20), unique=True, nullable=False)
    infractions = db.relationship('Infraction', backref='official', lazy=True)

class Infraction(db.Model):
    __tablename__ = 'infractions'
    id = db.Column(
        db.Integer, primary_key=True)
    timestamp = db.Column(
        db.DateTime, nullable=False)
    comments = db.Column(
        db.String(255), nullable=False)
    vehicle_id = db.Column(
        db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    official_id = db.Column(
        db.Integer, db.ForeignKey('officials.id'), nullable=False)