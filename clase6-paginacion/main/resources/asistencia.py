from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import animales_exhibicionesModel

#Recurso Proyecto
class Asitencias(Resource):
    #Insertar recurso
    def post(self):
        # Obtener objeto con id_animal y id_exhibicion
        id_animal = request.get_json().get('id_animal')
        id_exhibicion = request.get_json().get('id_exhibicion')

        # Verificar si los objetos existen
        if id_animal is None:
            print("Animal no encontrado")
            # Manejo de error o salida temprana si el animal no existe
        if id_exhibicion is None:
            print("Exhibición no encontrada")
            # Manejo de error o salida temprana si la exhibición no existe

        # Insertar una nueva entrada en la tabla secundaria para asociar el animal con la exhibición
        query = animales_exhibicionesModel.insert().values(id_animal=id_animal, id_exhibicion=id_exhibicion)
        try:
            # Ejecutar la consulta
            db.session.execute(query)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return 'Creado con exito', 201