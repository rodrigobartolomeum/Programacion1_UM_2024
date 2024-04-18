from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ExhibicionesModel

#Recurso Proyecto
class Exhibicion(Resource):
    #Obtener recurso
    def get(self, id):
        exhibicion = db.session.query(ExhibicionesModel).get_or_404(id)
        return exhibicion.to_json()
    #Eliminar recurso
    def delete(self, id):
        exhibicion = db.session.query(ExhibicionesModel).get_or_404(id)
        db.session.delete(exhibicion)
        db.session.commit()
        return '', 204
    #Modificar recurso
    def put(self, id):
        exhibicion = db.session.query(ExhibicionesModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(exhibicion, key, value)
        db.session.add(exhibicion)
        db.session.commit()
        return exhibicion.to_json() , 201

#Recurso Proyectos
class Exhibiciones(Resource):
    #Obtener lista de recursos
    def get(self):
        exhibiciones = db.session.query(ExhibicionesModel).all()
        
        return jsonify({ 'ExhibicionesModel': [exhibicion.to_json() for exhibicion in exhibiciones] })
    #Insertar recurso
    def post(self):
        exhibicion = ExhibicionesModel.from_json(request.get_json())
        print(exhibicion)
        try:
            db.session.add(exhibicion)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return exhibicion.to_json(), 201
