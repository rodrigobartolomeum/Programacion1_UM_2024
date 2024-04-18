from .. import db


animales_exhibiciones = db.Table("animales_exhibiciones",
    db.Column("id_animal",db.Integer,db.ForeignKey("animal.id"),primary_key=True),
    db.Column("id_exhibicion",db.Integer,db.ForeignKey("exhibicion.id"),primary_key=True)
    )

class Exhibicion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    puntaje_max = db.Column(db.Integer, nullable=True)
    animales = db.relationship('Animal', secondary=animales_exhibiciones, backref=db.backref('exhibiciones', lazy='dynamic'))
    
    def __repr__(self):
        return '<Exhibicion: %r %r >' % (self.descripcion,self.tipo)
    #Convertir objeto en JSON
    def to_json(self):
        #me aseguro que realmente existe el id animal (por si esta credo la tabla anteriormente con un animal q no existe)
        exhibiciones_json = {
            'id': self.id,
            'descripcion': str(self.descripcion),
            'tipo': str(self.tipo),
            'animales' : [animal.to_json() for animal in self.animales]
        }
        return exhibiciones_json
    
    @staticmethod
    #Convertir JSON a objeto
    def from_json(exhibiciones_json):
        id = exhibiciones_json.get('id')
        descripcion = exhibiciones_json.get('descripcion')
        tipo = exhibiciones_json.get('tipo')
        return Exhibicion(id=id,
                    descripcion=descripcion,
                    tipo=tipo
                    )
