from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import HistoriaClinicaModel

#Recurso Proyecto
class HistoriaClinica(Resource):
    #Obtener recurso
    def get(self, id):
        historia = db.session.query(HistoriaClinicaModel).get_or_404(id)
        return historia.to_json()
    #Eliminar recurso
    def delete(self, id):
        historia = db.session.query(HistoriaClinicaModel).get_or_404(id)
        db.session.delete(historia)
        db.session.commit()
        return '', 204
    #Modificar recurso
    def put(self, id):
        historia = db.session.query(HistoriaClinicaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(historia, key, value)
        db.session.add(historia)
        db.session.commit()
        return historia.to_json() , 201

#Recurso Proyectos
class HistoriasClinicas(Resource):
    #Obtener lista de recursos
    def get(self):
        #Obtener valores del request
        id_animal = request.args.get('id_animal')
        
        #filters =  request.data
        
        #Que le falta esta linea para retornar todas las historias clinicas
        historias = db.session.query(HistoriaClinicaModel)
        #Verificar si hay filtros
        
        if id_animal:
            historias = historias.filter(HistoriaClinicaModel.id_animal == id_animal)
        # if filters:
        #     #Recorrer filtros
        #     for key, value in request.get_json().items():
        #         if key == "id_animal":
        #             historias = historias.filter(HistoriaClinicaModel.id_animal == value)
        
        
        #finalmete con los filtros aplicados hago el all
        #tambien se puede manejar la paginacion
        historias = historias.all()

        return jsonify({ 'historias': [historia.to_json() for historia in historias] })
    #Insertar recurso
    def post(self):
        historia = HistoriaClinicaModel.from_json(request.get_json())
        print(historia)
        try:
            db.session.add(historia)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return historia.to_json(), 201
