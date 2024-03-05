import unittest
import logging

logging.basicConfig(level=logging.DEBUG)

from testing.test_data_inserts import TestDataInserts
from testing.test_data_selects import TestDataSelects

def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestDataInserts))
 #   suite.addTest(loader.loadTestsFromTestCase(TestDataSelects))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
