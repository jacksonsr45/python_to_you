import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Message(db.Model, SerializerMixin):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    subject = db.Column(db.String(255))
    message = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())