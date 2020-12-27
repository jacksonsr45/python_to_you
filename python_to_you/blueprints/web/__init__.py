from flask import Blueprint

from .views import index


def init_app(app):
    app.add_url_rule("/", "index", index)