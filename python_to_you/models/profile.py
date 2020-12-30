import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Profile(db.Model, SerializerMixin):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id', ondelete="CASCADE"))
    addresses_id = db.Column(db.ForeignKey('addresses.id', ondelete="CASCADE"))
    name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    social_media = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())


class ProfilePicture(db.Model, SerializerMixin):
    __tablename__ = 'profiles_images'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.ForeignKey('profiles.id', ondelete="CASCADE"))
    title = db.Column(db.String(255))
    path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())