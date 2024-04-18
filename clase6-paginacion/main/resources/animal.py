from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AnimalModel, HistoriaClinicaModel, ExhibicionesModel
from sqlalchemy import func, desc

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
        #Página inicial por defecto
        page = 1
        #Cantidad de elementos por página por defecto
        per_page = 10
        
        #no ejecuto el .all()
        animales = db.session.query(AnimalModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        #Si necesito traer los animales que la cantidad de los registros de la historia clinica se mayor o igual a nrHistoriasClinicas, puedo armar un filtro como el siguiente
        if request.args.get('nrHistoriasClinicas'):
            animales=animales.outerjoin(AnimalModel.historias).group_by(AnimalModel.id).having(func.count(HistoriaClinicaModel.id) >= int(request.args.get('nrHistoriasClinicas')))
        
        #Busqueda por raza
        if request.args.get('raza'):
            animales=animales.filter(AnimalModel.raza.like("%"+request.args.get('raza')+"%"))
        
        #Ordeno por raza
        if request.args.get('sortby_raza'):
            animales=animales.order_by(desc(AnimalModel.raza))
            
        #Ordeno por id de historias clinicas
        if request.args.get('sortby_nrHistoriasClinicas'):
            animales=animales.outerjoin(AnimalModel.historias).group_by(AnimalModel.id).order_by(func.count(HistoriaClinicaModel.id).desc())
        
        ### FIN FILTROS ####
        
        
        #Obtener valor paginado
        animales = animales.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'animales': [animal.to_json() for animal in animales],
                  'total': animales.total,
                  'pages': animales.pages,
                  'page': page
                })

    #insertar recurso
    def post(self):
        exhibiciones_ids = request.get_json().get('exhibiciones')
        animal = AnimalModel.from_json(request.get_json())
        
        if exhibiciones_ids:
            # Obtener las instancias de Exhibicion basadas en las ids recibidas
            exhibiciones = ExhibicionesModel.query.filter(ExhibicionesModel.id.in_(exhibiciones_ids)).all()
            # Agregar las instancias de Exhibicion a la lista de exhibiciones del Animal
            animal.exhibiciones.extend(exhibiciones)
            
        db.session.add(animal)
        db.session.commit()
        return animal.to_json(), 201

        