import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_positive_scenario_audio_provided(self):
        # Test positive scenario where audio file is provided
        with open('test_audio.wav', 'rb') as audio_file:
            response = self.app.post('/predict', data={'audio': (audio_file, 'test_audio.wav')})
            data = response.json
            self.assertEqual(response.status_code, 200)
            self.assertIn('transcript', data)
            self.assertIn('sentiment', data)
            self.assertIn('emotion', data)
            # Add more assertions based on expected behavior

    def test_negative_scenario_no_audio_provided(self):
        # Test scenario where no audio file is provided
        response = self.app.post('/predict')
        data = response.json
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'No audio file provided.')

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

    def test_negative_scenario_large_audio_file(self):
        # Test scenario where a large audio file is provided
        with open('large_audio.wav', 'rb') as audio_file:
            response = self.app.post('/predict', data={'audio': (audio_file, 'large_audio.wav')})
            data = response.json
            self.assertEqual(response.status_code, 200)
            self.assertIn('error', data)
            self.assertEqual(data['error'], 'Audio file size exceeds the limit.')

if __name__ == '__main__':
    unittest.main()
