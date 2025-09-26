import unittest
from app import convert_audio_to_text, preprocess_text

class TestAppFunctions(unittest.TestCase):
    def test_convert_audio_to_text_pass(self):
        # Provide a valid test audio file
        audio_path = '16.wav'
        text = convert_audio_to_text(audio_path)
        self.assertIsInstance(text, str)

if __name__ == '__main__':
    unittest.main()
