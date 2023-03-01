
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from flask import current_app

from flask import Blueprint, request, jsonify

from .models import db, Person, Vehicle, Official, Infraction

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/generate_report/<email>', methods=['GET'])
def generate_report(email):
    person = Person.query.filter_by(email=email).first()
    if person is None:
        return jsonify({'message': 'No person found with that email address'})

    vehicles = person.vehicles
    infractions = []
    for vehicle in vehicles:
        vehicle_infractions = Infraction.query.filter_by(vehicle_id=vehicle.id).all()
        for infraction in vehicle_infractions:
            infr = {
                'plate_number': vehicle.license_plate, 
                'timestamp': infraction.timestamp, 
                'comments': infraction.comments
            }
            infractions.append(infr)

    if not infractions:
        return jsonify({'message': 'No infractions found for vehicles registered to that email address'})
    
    return jsonify(infractions)

@api.route('/login', methods=['POST'])
def login():
    # Check if request content type is valid
    if not request.content_type.startswith('multipart/form-data'):
        return jsonify({'error': 'Invalid content type form-data'}), 400

    # Obtener los valores de los campos del formulario
    username = request.form.get('username')
    password = request.form.get('password')

    # Verificar que los valores no sean nulos
    if not username or not password:
        return jsonify({'error': 'Invalid username or password'}), 400
    
    # Verificar las credenciales del usuario (ejemplo)
    if username == "DiegoUG" and password == "mi_contraseña":
        # Generar un token JWT con los datos del usuario
        secret_key = current_app.config['JWT_SECRET_KEY']
        token = create_access_token({'username': 'DiegoUG'}, secret_key)
        # Devolver el token JWT al usuario
        return jsonify({'token': token}), 200
    else:
        # Devolver un mensaje de error si las credenciales son inválidas
        return jsonify({'error': 'Credenciales inválidas'}), 401

@api.route('/infraction', methods=['POST'])
@jwt_required()
def create_infraction():
    try:
        plate_number = request.json['placa_patente']
        timestamp = request.json['timestamp']
        comments = request.json['comentarios']

        vehicle = Vehicle.query.filter_by(license_plate=plate_number).first()
        if not vehicle:
            return jsonify({'message': 'No vehicle found with that plate number'}), 404

        official_token = get_jwt_identity()
        official = Official.query.filter_by(
            name=official_token['username']).first()
        if official is None:
            return jsonify({'message': 'Infraction created successfully!'})

        infraction = Infraction(
            timestamp=timestamp, 
            comments=comments, 
            vehicle_id=vehicle.id, 
            official_id=official.id)
        
        db.session.add(infraction)
        db.session.commit()

        return jsonify({'message': 'Infraction created successfully!'})

    except KeyError:
        return jsonify({'message': 'Missing or incorrect parameter in request body'}), 400
    except:
        return jsonify({'message': 'Unexpected error occurred'}), 500
