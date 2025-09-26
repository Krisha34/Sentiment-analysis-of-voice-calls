import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_positive_scenario_audio_provided(self):
        # Test positive scenario where audio file is provided
        with open('Audios/angry3.wav', 'rb') as audio_file:
            response = self.app.post('/predict', data={'audio': (audio_file, 'Audios/angry3.wav')})
            data = response.json
            self.assertEqual(response.status_code, 200)
            self.assertIn('transcript', data)
            self.assertIn('sentiment', data)
            self.assertIn('emotion', data)
            # Add more assertions based on expected behavior
    def test_index_page_loads_successfully(self):
        # Test if the index page loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sentiment Analysis of Voice Calls', response.data)




if __name__ == '__main__':
    unittest.main()
