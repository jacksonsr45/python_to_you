import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    is_admin = db.Column(db.Boolean(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())