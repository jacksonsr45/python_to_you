from flask_script import Manager, Command
from flask import Flask
from dynaconf import FlaskDynaconf
from flask_migrate import MigrateCommand
from python_to_you.extensions import configuration


_app = Flask(
            "python_to_you", 
            template_folder="blueprints/templates",
            static_folder="blueprints/static"
        )

FlaskDynaconf(_app)
manager = Manager(_app)

configuration.load_extensions(_app)

@manager.command
def create_app():
    _app.run(debug=True, load_dotenv=True)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', create_app())