from typing import NoReturn
from flask_bootstrap import Bootstrap

##
# Init appearance with Bootstrap
# @param app
# @return none
# #
def init_app(app) -> NoReturn:
    Bootstrap(app)
    