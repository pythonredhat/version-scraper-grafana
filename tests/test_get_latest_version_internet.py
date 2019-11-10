import unittest
from unittest import mock
from unittest.mock import patch, Mock
import requests
import os
from .data import ansible
from version_scraper_grafana.get_latest_version_internet import get_latest_version_internet

#TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'data/ansible.json')

class MyTest(unittest.TestCase):
    
    def test_getting_internet_version_when_response_ok(self):
        
        #define the patch for requests.get method
        mock_get_patcher = patch('version_scraper_grafana.get_latest_version_internet.requests.get')

        #define response data from github
        data = {"name": "6.0.0"}

        #start the patch
        mock_get = mock_get_patcher.start()

        #define response data for my Mock object
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = data

        #call regular function
        response = get_latest_version_internet()

        #stop the patch
        mock_get_patcher.stop()

        #assert the request-response cycle completed successfully
        self.assertEqual(response, "6.0.0")

#main link i am working off for code above
#https://stackoverflow.com/questions/50157543/unittest-django-mock-external-api-what-is-proper-way


###link i am working off to improve/simplify code
#https://auth0.com/blog/mocking-api-calls-in-python/

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