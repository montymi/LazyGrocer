import unittest
import logging
import argparse

from testing.test_data_inserts import TestDataInserts
from testing.test_data_selects import TestDataSelects

def test_suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(TestDataInserts))
    suite.addTest(loader.loadTestsFromTestCase(TestDataSelects))
    return suite

if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser(description='Run unit tests with different logging levels')
    parser.add_argument('-D', '--debug', action='store_const', const=logging.DEBUG, dest='log_level', 
                        help='Set logging level to DEBUG')
    parser.add_argument('-I', '--info', action='store_const', const=logging.INFO, dest='log_level', 
                        help='Set logging level to INFO (default)')
    parser.add_argument('-W', '--warning', action='store_const', const=logging.WARNING,dest='log_level', 
                        help='Set logging level to WARNING')
    parser.add_argument('-E', '--error', action='store_const', const=logging.ERROR, dest='log_level', 
                        help='Set logging level to ERROR')
    parser.add_argument('-C', '--critical', action='store_const', const=logging.CRITICAL, dest='log_level',
                        help='Set logging level to CRITICAL')
    args = parser.parse_args()

    if args.log_level is not None:
        logging.basicConfig(level=args.log_level)
    else:
        logging.basicConfig(level=logging.INFO)

    # run tests in test_suite()
    runner = unittest.TextTestRunner()
    runner.run(test_suite())
