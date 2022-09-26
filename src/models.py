from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favoritos_per = db.relationship('FavoritosPer', backref='user')
    favoritos_pla = db.relationship("FavoritosPla", backref="user")

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

    class Personajes(db.Model):
        __tablename__ = 'personajes'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        clasificacion = db.Column(db.String(250), nullable=False)
        lenguaje = db.Column(db.String(50), nullable=False)
        creacion = db.Column(db.String(10), nullable=False)
        favorite_personaje_id = db.Column(db.Integer, db.ForeignKey('favoritosPer.id'))
        

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "clasificacion" : self.clasificacion,
            "lenguaje" : self.lenguaje,
            "creacion" : self.creacion

        }

    class Planetas(db.Model):
        __tablename__ = 'planetas'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(50), nullable=False)
        gravedad = db.Column(db.String(50), nullable=False)
        favoriteplanet_id = db.Column(db.Integer, db.ForeignKey('favoritosplanet.id'))

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

    class FavoritosPer(db.Model):
        __tablename__ = 'favoritosPer'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        Character = db.relationship("Personajes",backref="favorite")     

    def serialize(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "personaje_id" : self.personaje_id
            }

    class FavoritosPla(db.Model):
        __tablename__ = 'favoritosplanet'
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        planet = db.relationship("Planetas",backref="favorite")
        
    def serialize(self):
            return {
                "id": self.id,
                "user_id": self.user_id,
                "planeta_id" : self.planeta_id
            }