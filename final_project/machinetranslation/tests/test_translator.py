import unittest
from ../translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english("Bonjour"), None)
        self.assertEqual(french_to_english("Bonjour"),"Hello")

    def test_english_to_french(self):
        self.assertNotEqual(english_to_french("Hello"), None)
        self.assertEqual(english_to_french("Hello"),"Bonjour")

if __name__=='__main__':
    unittest.main()