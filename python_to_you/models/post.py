import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Post(db.Model, SerializerMixin):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.ForeignKey('profiles.id', ondelete="CASCADE"))
    category_id = db.Column(db.ForeignKey('categories.id', ondelete="CASCADE"))
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    description = db.Column(db.Text())
    text = db.Column(db.Text())
    key_words = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())


class PostPicture(db.Model, SerializerMixin):
    __tablename__ = 'posts_pictures'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.ForeignKey('posts.id', ondelete="CASCADE"))
    title = db.Column(db.String(255))
    path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())