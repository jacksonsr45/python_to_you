import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Groups(db.Model, SerializerMixin):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'))
    create_post = db.Column(db.Boolean(),default=False)
    edit_post = db.Column(db.Boolean(),default=False)
    update_post = db.Column(db.Boolean(),default=False)
    read_post = db.Column(db.Boolean(),default=True)
    add_post = db.Column(db.Boolean(),default=False)
    remove_post = db.Column(db.Boolean(),default=False)
    block_post = db.Column(db.Boolean(),default=False)
    title = db.Column(db.String(255))
    description = db.Column(db.Text())
    social_media = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())