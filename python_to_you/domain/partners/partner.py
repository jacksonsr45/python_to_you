import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Partner(db.Model, SerializerMixin):
    __tablename__ = 'partners'
    id = db.Column(db.Integer, primary_key=True)
    commit = db.Column(db.Text())
    description = db.Column(db.Text())
    slug = db.Column(db.String(255))
    url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())


class PartnerImage(db.Model, SerializerMixin):
    __tablename__ = 'partners_images'
    id = db.Column(db.Integer, primary_key=True)
    partner_id = db.Column(db.ForeignKey('partners.id'))
    title = db.Column(db.String(255))
    path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())