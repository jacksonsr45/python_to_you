from typing import NoReturn
from importlib import import_module
from dynaconf import FlaskDynaconf


##
# Load all extensions in settings.toml
# @param app
# @return none
# #
def load_extensions(app) -> NoReturn:
    for extension in app.config.EXTENSIONS:
        mod = import_module(extension)
        mod.init_app(app)


##
# Init Configuration with dynaconf
# @param app
# @return none
# #
def init_app(app, **config) -> NoReturn:
    FlaskDynaconf(app, **config)