from flask.app import Flask
from unittest import TestCase
from python_to_you import app


class TestAppFactory(TestCase):
    def test_if_has_in_app_a_minimal_app(self):
        self.assertEqual(
            hasattr(app, 'minimal_app'),
            True,
            'Do not has a minimal_app in app!'
        )

    def test_if_has_in_app_a_create_app(self):
        self.assertEqual(
            hasattr(app, 'create_app'),
            True,
            'Do not has a create_app in app!'
        )

    def test_if_create_app_has_a_call(self):
        self.assertEqual(
            hasattr(app.create_app, '__call__'),
            True,
            'create_app do not has a call!'
        )

    def test_create_app_is_instance_by_flask(self):
        self.assertIsInstance(
            app.create_app(),
            Flask,
            'create_app do not has a instance by Flask'
        )