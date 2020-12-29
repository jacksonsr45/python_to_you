import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class LikeDislike(db.Model, SerializerMixin):
    __tablename__ = 'likes_dislikes'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.ForeignKey('profiles.id'))
    post_id = db.Column(db.ForeignKey('posts.id'))
    select_like = db.Column(db.Enum("like", "deslike", "null"))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())