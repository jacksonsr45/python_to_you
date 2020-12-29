from typing import NoReturn
from flask_migrate import Migrate
from python_to_you.extensions.database import db

migrate = Migrate()

##
# Init migrate
# @param app
# @return none
# #
def init_app(app) -> NoReturn:
    migrate.init_app(app, db)