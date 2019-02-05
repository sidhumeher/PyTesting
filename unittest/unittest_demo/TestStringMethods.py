'''
Created on Feb 4, 2019

@author: siddardha.teegela
'''
import unittest

# Testcase is creating by subclassing unittest.TestCase

class TestStringMethods(unittest.TestCase):
    
    #setUp and tearDown runs for every testcase
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        print('Method to do test setup')
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        print('Method to tead down after test')

    def test_upper(self):
        self.assertEqual('teststring'.upper(), 'TESTSTRING', 'Strings are same')
        
    def test_isUpper(self):
        self.assertTrue('TESTSTRING'.isupper())
        self.assertFalse('teststring'.isupper())

    def test_split(self):
        s = 'test string'
        self.assertEqual(s.split(), ['test','string'])
        
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(9)

if __name__ == '__main__':
    unittest.main()