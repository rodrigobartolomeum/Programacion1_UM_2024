from .. import db
from datetime import datetime

#Importamos de python 2 funciones
from werkzeug.security import generate_password_hash, check_password_hash

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(100), nullable=False)
    fechaNac = db.Column(db.DateTime, nullable=False)
    #Mail usado como nombre de usuario
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
    #Contraseña que será el hash de la pass en texto plano
    password = db.Column(db.String(128), nullable=False)
    #Rol (En el caso que existan diferentes tipos de usuarios/animales con diferentes permisos)
    rol = db.Column(db.String(10), nullable=False, server_default="users")
    #nombre de la relacion (historias)
    historias = db.relationship("HistoriaClinica", back_populates="animal",cascade="all, delete-orphan")
    
    #Getter de la contraseña plana no permite leerla
    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<Animal: %r >' % (self.raza)
    #Convertir objeto en JSON
    def to_json(self):
        animal_json = {
            'id': self.id,
            'name': str(self.name),
            'raza': str(self.raza),
            'fechaNac': str(self.fechaNac.strftime("%d-%m-%Y")),
            'email': str(self.email)
        }
        return animal_json
    
    def to_json_complete(self):
        historias = [historia.to_json() for historia in self.historias]
        animal_json = {
            'id': self.id,
            'name': str(self.name),
            'raza': str(self.raza),
            'fechaNac': str(self.fechaNac.strftime("%d-%m-%Y")),
            'historias':historias

        }
        return animal_json

    def to_json_short(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

        }
        return animal_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(animal_json):
        id = animal_json.get('id')
        name = animal_json.get('name')
        raza = animal_json.get('raza')
        #con el strptime lo convierto a un objeto datetime de python
        fechaNac = datetime.strptime(animal_json.get('fechaNac'), '%d-%m-%Y')
        email = animal_json.get('email')
        password = animal_json.get('password')
        rol = animal_json.get('rol')
        return Animal(id=id,
                    name=name,
                    raza=raza,
                    fechaNac = fechaNac,
                    email=email,
                    plain_password=password,
                    rol=rol
                    )
