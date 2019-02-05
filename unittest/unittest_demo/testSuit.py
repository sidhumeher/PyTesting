'''
Created on Feb 4, 2019

@author: siddardha.teegela
'''

import unittest
from unittest import runner
from unittest_demo.TestStringMethods import TestStringMethods

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test_upper'))
    suite.addTest(TestStringMethods('test_isUpper'))
    suite.addTest(TestStringMethods('test_split'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())