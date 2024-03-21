# Al app.py no vamos a tener que agregarle nada

from main import create_app
import os

#Llamamos a la funcion que retorna la app
app = create_app()

# Hay que hacer push del contexto de la app
# Con esto la app quead disponible en todo los archivos
# Nos permite no tener conflictos con referencias circulares
# Recursividad en las importaciones

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv('PORT'))