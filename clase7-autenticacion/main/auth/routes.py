from flask import request, jsonify, Blueprint
from .. import db
from main.models import AnimalModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

#Blueprint para acceder a los métodos de autenticación
auth = Blueprint('auth', __name__, url_prefix='/auth')

#Método de logueo
@auth.route('/login', methods=['POST'])
def login():
    #Busca al animal en la db por mail
    animal = db.session.query(AnimalModel).filter(AnimalModel.email == request.get_json().get("email")).first_or_404()
    #Valida la contraseña
    if animal.validate_pass(request.get_json().get("password")):
        #Genera un nuevo token
        #Pasa el objeto animal como identidad
        access_token = create_access_token(identity=animal)
        #Devolver valores y token
        data = {
            'id': str(animal.id),
            'email': animal.email,
            'access_token': access_token
        }

        return data, 200
    else:
        return 'Incorrect password', 401

#Método de registro
@auth.route('/register', methods=['POST'])
def register():
    #Obtener animal
    animal = AnimalModel.from_json(request.get_json())
    #Verificar si el mail ya existe en la db, scalar() para saber la cantidad de ese email
    exists = db.session.query(AnimalModel).filter(AnimalModel.email == animal.email).scalar() is not None
    if exists:
        return 'Duplicated mail', 409
    else:
        try:
            #Agregar animal a DB
            db.session.add(animal)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return animal.to_json() , 201
