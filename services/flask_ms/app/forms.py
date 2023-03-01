from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

# Formulario para crear y editar una persona
class PersonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# Formulario para crear y editar un vehículo
class VehicleForm(FlaskForm):
    license_plate = StringField('License Plate', validators=[DataRequired()])
    brand = StringField('Brand', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    owner = SelectField('Owner', coerce=int)
    submit = SubmitField('Submit')

# Formulario para crear y editar un oficial
class OfficialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    identification_number = StringField('Identification Number', validators=[DataRequired()])
    submit = SubmitField('Submit')
