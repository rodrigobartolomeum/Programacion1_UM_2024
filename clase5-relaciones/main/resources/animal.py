from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AnimalModel

# #Datos de prueba en JSON
# ANIMALES = {
#     1: {'nombre':'Boby', 'raza':'Obejero Aleman'},
#     2: {'nombre':'Peter', 'raza':'Caniche'}
# }

#Defino el recurso Animal
class Animal(Resource): #A la clase animal le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
    def get(self, id):
        animal = db.session.query(AnimalModel).get_or_404(id)
        return animal.to_json_complete()

    #eliminar recurso
    def delete(self, id):
        animal = db.session.query(AnimalModel).get_or_404(id)
        db.session.delete(animal)
        db.session.commit()
        return '', 204

    #Modificar el recurso animal
    def put(self, id):
        animal = db.session.query(AnimalModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(animal, key, value)
        db.session.add(animal)
        db.session.commit()
        return animal.to_json() , 201


#Coleccion de recurso Animales
class Animales(Resource):
    #obtener lista de los animales
    def get(self):
        animales = db.session.query(AnimalModel).all()
        return jsonify([animal.to_json() for animal in animales])

    #insertar recurso
    def post(self):
        animal = AnimalModel.from_json(request.get_json())
        db.session.add(animal)
        db.session.commit()
        return animal.to_json(), 201

        