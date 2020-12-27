from unittest import TestCase
from python_to_you import app

class FlaskBaseTestCase(TestCase):
    def setUp(self):
        self.app = app.create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()