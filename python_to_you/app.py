from python_to_you.extensions import configuration
from flask import Flask


##
# Init minimal_app
# This is required in tests
# @param none
# @return Flask app
# #
def minimal_app():
    app = Flask(
            __name__, 
            template_folder="blueprints/templates",
            static_folder="blueprints/static"
        )
    configuration.init_app(app)
    return app


##
# This is a factory
# Create app and load all extensions
# @param none
# @return Flask app
# #
def create_app():
    app = minimal_app()
    configuration.load_extensions(app)
    return app 