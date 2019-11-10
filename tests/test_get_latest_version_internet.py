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
        #define new mock object
        mock_response = mock.Mock()
        #define response data from github
        data = {"name": "6.0.0"}

        #define response data for my Mock object
        mock_response.json.return_value = data
        mock_response.status_code = 200

        #define response data for the fake API
        mock_get.return_value = mock_response 

        #call regular function
        result = get_latest_version_internet()

        self.assertEqual(result, "6.0.0")
        #need to work on status code
        #self.assertEqual(result.status_code, 200)


#main link i am working off for code above
#https://stackoverflow.com/questions/50157543/unittest-django-mock-external-api-what-is-proper-way


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