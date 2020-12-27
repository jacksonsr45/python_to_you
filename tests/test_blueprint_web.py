from flask.app import Flask
from flask import render_template
from tests.flask_base_test_case import FlaskBaseTestCase
from python_to_you.blueprints import web


class TestBluePrintWeb(FlaskBaseTestCase):
    def test_if_blueprint_web_has_index(self):
        self.assertEqual(
            hasattr(web, 'index'),
            True,
            'web do not has a index!'
        )

    def test_if_index_has_a_call(self):
        self.assertEqual(
            hasattr(web.index, "__call__"),
            True,
            'index do not has a call!'
        )

    def test_if_index_return_render_template(self):
        test = web.index()
        self.assertEqual(
            test,
            render_template("index.html", title="Home"),
            'Do not has return a render template valid!'
        )