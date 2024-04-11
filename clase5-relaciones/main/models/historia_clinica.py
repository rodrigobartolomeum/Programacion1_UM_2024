from .. import db
from . import AnimalModel

class HistoriaClinica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    #Clave foranea (esto debe ir en los n o muchos)
    id_animal = db.Column(db.Integer, db.ForeignKey("animal.id"), nullable=False)
    #nombre de la relacion (animal)
    animal = db.relationship("Animal", back_populates="historias", uselist=False, single_parent=True)
    
    def __repr__(self):
        return '<HistoriaClinica: %r %r >' % (self.id_animal, self.descripcion)
    #Convertir objeto en JSON
    def to_json(self):
        #me aseguro que realmente existe el id animal (por si esta credo la tabla anteriormente con un animal q no existe)
        self.animal = db.session.query(AnimalModel).get_or_404(self.id_animal)
        historia_json = {
            'id': self.id,
            'descripcion': str(self.descripcion),
            'animal' : self.animal.to_json() #le paso el animal pasado a JSON / tengo todos lo datos juntos
        }
        return historia_json

    def to_json_short(self):
        historia_json = {
            'id': self.id,
            'descripcion': str(self.descripcion),

        }
        return historia_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(historia_json):
        id = historia_json.get('id')
        descripcion = historia_json.get('descripcion')
        id_animal = historia_json.get('id_animal')
        return HistoriaClinica(id=id,
                    descripcion=descripcion,
                    id_animal=id_animal
                    )
