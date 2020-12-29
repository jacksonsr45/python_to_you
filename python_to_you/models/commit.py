import datetime
from python_to_you.extensions.database import db
from sqlalchemy_serializer import SerializerMixin


class Commit(db.Model, SerializerMixin):
    __tablename__ = 'commits'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.ForeignKey('profiles.id'))
    post_id = db.Column(db.ForeignKey('posts.id'))
    commit = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())



class CommitResponse(db.Model, SerializerMixin):
    __tablename__ = 'commits_responses'
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.ForeignKey('profiles.id'))
    commit_id = db.Column(db.ForeignKey('commits.id'))
    commit = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime())