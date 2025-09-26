import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_negative_scenario_empty_audio_file(self):
        # Test scenario where an empty audio file is provided
        with open('empty_audio.wav', 'rb') as audio_file:
            response = self.app.post('/predict', data={'audio': (audio_file, 'empty_audio.wav')})
            data = response.json
            self.assertEqual(response.status_code, 200)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Empty audio file provided.')

    def test_negative_scenario_invalid_file_format(self):
        # Test scenario where an invalid file format is provided
        with open('test_pdf.pdf', 'rb') as audio_file:
            response = self.app.post('/predict', data={'audio': (audio_file, 'test_pdf.pdf')})
            data = response.json
            self.assertEqual(response.status_code, 200)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Invalid file format.')



if __name__ == '__main__':
    unittest.main()
