import requests
from bs4 import BeautifulSoup
from .config import *
import json

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="./logs/test.log")


def versionlord_updater(latest_version_internet, latest_version_versionlord):
    try:
        if latest_version_internet == latest_version_versionlord:
            print("All good in the hood!") 
        else:
            print(f"Version Lord is not up to date with {software}'s website on the internet")
            data = {'current_version': latest_version_internet, 'software': software}
            payload = requests.put(url=url_version_lord, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            logging.debug(payload.status_code)
            logging.debug(payload.content)
    except Exception as ex:
        logging.exception('caught an error')

if __name__ == "__main__":
    versionlord_updater(latest_version_internet, latest_version_versionlord)