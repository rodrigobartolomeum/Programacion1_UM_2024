import os
from flask import Flask
from dotenv import load_dotenv

#Importamos nuevas librerias clase 3
from flask_restful import Api #Agrego la clase API

#Importar SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Inicializar API de Flask Restful
api = Api()
#Inicializar SQLAlchemy
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    #Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)
    migrate.init_app(app,db)

    #Importar directorio de recursos
    import main.resources as resources

    #cargar a la API el recurso Animales y especificar la ruta 
    api.add_resource(resources.AnimalesResource, '/animales')
    #cargar a la API el recurso Animal y especificar la ruta 
    api.add_resource(resources.AnimalResource, '/animal/<id>')
    api.add_resource(resources.HistoriasClinicasResource, '/historias')
    api.add_resource(resources.HistoriaClinicaResource, '/historia/<id>')
    api.add_resource(resources.ExhibicionesResource, '/exhibiciones')
    api.add_resource(resources.ExhibicionResource, '/exhibicion/<id>')
    api.add_resource(resources.AsistensiasResource, '/asistencias')
    
    
    
    
    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)
    #Por ultimo retornamos la aplicacion iniializada
    return app