import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_welcome_message(self):
        response = self.app.get('/')
        expected_message = 'Welcome to our Application!'
        self.assertIn(expected_message, response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
