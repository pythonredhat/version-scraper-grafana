import unittest
from unittest import mock
from unittest.mock import patch, Mock
import requests
import os
from .data import ansible
from version_scraper_grafana.get_latest_version_internet import get_latest_version_internet

#TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data/ansible.json')

class MyTest(unittest.TestCase):
    
    @mock.patch('version_scraper_grafana.get_latest_version_internet.requests.get')
    def test_getting_internet_version_when_response_ok(self, mock_get):
        mock_response = mock.Mock()
        data = {"name": "6.0.0"}

        mock_response.json.return_value = data
        mock_response.status_code = 200 

        mock_get.return_value = mock_response 

        result = get_latest_version_internet()

        self.assertEqual(result, "6.0.0")
         #assert_list_equal(response.json(), data)


#main link i am working off for code above
#https://stackoverflow.com/questions/50157543/unittest-django-mock-external-api-what-is-proper-way





#    def setUp(self):
#        self.testfile = open(TESTDATA_FILENAME)
#        self.testdata = self.testfile.read()
#        
#    def test_mock_whole_function(self):

    #"""Mocking a whole function"""
    #mock_get_patcher = patch('get_latest_version_internet')
    #users = self.testdata

    # start patching 'get_latest_version_internet'
    #mock_get = mock_get_patcher.start()

    #configure the mock to return a response with status code 200
    #mock_get.return_value = Mock(status_code = 200)
    #mock_get.return_value.json.return_value = users

    # call the service, which will send a request to the server
    #response = get_latest_version_internet()

    
    #def tearDown(self):
    #    self.testfile.close()

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