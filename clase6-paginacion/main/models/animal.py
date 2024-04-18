from .. import db
import json
from datetime import datetime

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    raza = db.Column(db.String(100), nullable=False)
    fechaNac = db.Column(db.DateTime, nullable=False)
    #nombre de la relacion (historias)
    historias = db.relationship("HistoriaClinica", back_populates="animal",cascade="all, delete-orphan")
    
    def __repr__(self):
        return '<Animal: %r >' % (self.raza)
    #Convertir objeto en JSON
    def to_json(self):
        animal_json = {
            'id': self.id,
            'name': str(self.name),
            'raza': str(self.raza),
            'fechaNac': str(self.fechaNac.strftime("%d-%m-%Y"))
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
        return Animal(id=id,
                    name=name,
                    raza=raza,
                    fechaNac = fechaNac
                    )
