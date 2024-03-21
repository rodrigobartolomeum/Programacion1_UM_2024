# La carpeta main va a tener todo el codigo menos app.py
from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

#Importar el directorio de recursos
import main.resources as resources

# Inicializar la API de flask RestFul
api = Api()

#Vamos a crear un metodo que inicializara la app y todos los modulos
def create_app():
    #Inicio flask
    app = Flask(__name__)

    #cargamos las variables del archivo .env
    load_dotenv()
     #cargar a la API el recurso Animales y especificar la ruta 
    api.add_resource(resources.AnimalesResource, '/animales')
    #cargar a la API el recurso Animal y especificar la ruta 
    api.add_resource(resources.AnimalResource, '/animal/<id>')
    
    #Cargar la aplicacion en la API de Flask Restful
    #es para que la aplicacion de flask funcione como API
    api.init_app(app)
    #Por ultimo retornamos la aplicacion iniializada
    return app