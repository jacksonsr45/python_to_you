from typing import NoReturn
from flask_sqlalchemy import SQLAlchemy

##
# Create instance SQLAlchemy in var db
# #
db = SQLAlchemy()

##
# Init Database with SQLAlchemy
# @param app
# @return none
# #
def init_app(app) -> NoReturn:
    db.init_app(app)