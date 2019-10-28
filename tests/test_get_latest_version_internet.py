import unittest
import requests
import os
from version_scraper_apache_kafka.get_latest_version_internet import parse_html

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data/kafka.html')

class MyTest(unittest.TestCase):

    def setUp(self):
        self.testfile = open(TESTDATA_FILENAME)
        self.testdata = self.testfile.read()

    def test_parse_html(self):
        testversion = parse_html(self.testdata, mode="test")
        self.assertEqual(testversion, "2.3.1")

    def tearDown(self):
        self.testfile.close()

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