import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin

class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(255))
    zip_code = db.Column(db.String(255))
    state = db.Column(db.String(255))
    city = db.Column(db.String(255))
    neighborhood = db.Column(db.String(255))
    number = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(),default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())