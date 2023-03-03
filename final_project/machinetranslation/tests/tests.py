import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        #englishText = "Hello"
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        self.assertNotEqual(englishToFrench('Null'), '')

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self): 
        #frenchText = "Bonjour"
        self.assertEqual(frenchToEnglish("Bonjour"), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        self.assertNotEqual(frenchToEnglish('Null'), '')

unittest.main()