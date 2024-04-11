from .. import db

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raza = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return ('<Animal: %r >' % (self.raza))
    
    #Convertir objeto en JSON
    def to_json(self):
        animal_json = {
            'id': self.id,
            'raza': str(self.raza),

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
        raza = animal_json.get('raza')
        return Animal(id=id,
                    raza=raza,
                    )
