import os
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
def runserver():
    _app.run(load_dotenv=True)


@manager.command
def unittest():
    os.system("python -m unittest discover tests/ -v")


@manager.command
def behave():
    os.system("behave tests/behavior/features/ -D debug=True")


@manager.command
def coverage():
    os.system("coverage run --source=python_to_you -m unittest discover tests/ -v")


@manager.command
def coverage_report():
    os.system("coverage report")


@manager.command
def coverage_html():
    os.system("coverage html")


manager.add_command('db', MigrateCommand)