from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    personal_number = db.Column(db.String(12), unique=True, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    cars = db.relationship('Car', backref='owner', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'personal_number': self.personal_number,
            'address': self.address
        }

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model_name = db.Column(db.String(50), nullable=False)
    model_year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20))
    registration_plate = db.Column(db.String(20), unique=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model_name': self.model_name,
            'model_year': self.model_year,
            'color': self.color,
            'registration_plate': self.registration_plate,
            'owner': self.owner.to_dict() if self.owner else None
        }