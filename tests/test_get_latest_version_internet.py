import unittest
import requests
import os
from version_scraper_apache_kafka.get_latest_version_internet import parse

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data/kafka.html')

class MyTest(unittest.TestCase):

    def setUp(self):
        self.testdata = open(TESTDATA_FILENAME).read()

    def test_get_latest_version_internet(self):
        testversion = parse(self.testdata)
        self.assertEqual(testversion, "2.3.1")

    #def tearDown(self):
     #   self.testdata.close()

if __name__ == "__main__":
    unittest.main()

'''
Given:
    some sample html (DONE)

When:
    run the function get_latest_version_internet (DONE)

Then:
    response is equal to 2.3.1 (DONE)
'''