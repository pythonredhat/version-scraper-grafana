import unittest
import requests
from configparser import ConfigParser
from importlib import resources

class MyTest(unittest.TestCase):

    def test_github(self):
        url = "https://api.github.com/repos/kubernetes/kubernetes/releases/latest"
        response = requests.get(url=url)
        print(response)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()