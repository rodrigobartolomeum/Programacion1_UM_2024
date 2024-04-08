from .. import db


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raza = db.Column(db.String(100), nullable=False)
    
    #Convertir objeto en JSON
    def to_json(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

        }
        return animal_json