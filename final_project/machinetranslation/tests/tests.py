import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/home/project/xzceb-flask_eng_fr/final_project/machinetranslation')))
#sys.path.append('/home/project/xzceb-flask_eng_fr/final_project/machinetranslation/translator.py')
import unittest
from translator import english_to_french, french_to_english

class Test_Translator(unittest.TestCase):
    def test_englishToFrench(self):
        #Test translation
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        #Test empty  string
        self.assertEqual(english_to_french(""), "")
    
    def test_frenchToEnglish(self):
        #Test traansaltion
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        #Test empty string
        self.assertEqual(french_to_english(""), "")
    
    def test_englishToFrench_null_input(self):
        #Test None input
        self.assertEqual(english_to_french(None), "")

    def test_frenchToEnglish_null_input(self):
        #Test None input
        self.assertEqual(french_to_english(None), "")

if __name__=='__main__':
    unittest.main()
    