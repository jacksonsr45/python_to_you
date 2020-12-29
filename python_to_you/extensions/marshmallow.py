from typing import NoReturn
from flask_marshmallow import Marshmallow

##
# Creating a instance of the Marshmallow in ma
# #
ma = Marshmallow()

##
# Init ma
# @param app
# @return none
# #
def init_app(app) -> NoReturn:
    ma.init_app(app)