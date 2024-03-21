from flask_restful import Resource
from flask import request

#Datos de prueba en JSON
ANIMALES = {
    1: {'nombre':'Boby', 'raza':'Obejero Aleman'},
    2: {'nombre':'Peter', 'raza':'Caniche'}
}

#Defino el recurso Animal
class Animal(Resource): #A la clase animal le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
    def get(self, id):
        #Verifico que exista el animal
        if int(id) in ANIMALES:
            #retorno animal
            return ANIMALES[int(id)]
        #Si no existe 404
        return '', 404
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el animal
        if int(id) in ANIMALES:
            #elimino animal
            del ANIMALES[int(id)]
            return '', 204
        #Si no existe 404
        return '', 404
    #Modificar el recurso animal
    def put(self, id):
        if int(id) in ANIMALES:
            animal = ANIMALES[int(id)]
            data = request.get_json()
            animal.update(data)
            return '', 201
        return '', 404

#Coleccion de recurso Animales
class Animales(Resource):
    #obtener lista de los animales
    def get(self):
        return ANIMALES
    #insertar recurso
    def post(self):
        animal = request.get_json()
        id = int(max(ANIMALES.keys()))+1
        ANIMALES[id] = animal
        return ANIMALES[id], 201