import requests
from .config import *
import logging
import sys
import json

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="./logs/scraper.log")

def get_latest_version_internet():

    try:
        response = requests.get(url=url_github_api)
        if response.status_code == 200:
            json_data = response.json()
            #json_data = json.loads(response.text)
            latest_version_internet = (json_data["name"])
        else:
            return None
    except requests.ConnectionError as e:
        logging.error(f"Unable to connect to Github")
        logging.exception(e)
        print(f"Unable to connect to Github")
        print(e)  
        sys.exit(1)
    except requests.Timeout as e:
        logging.error(f"It took too long to connect to Github, time out!")
        logging.exception(e)
        print(f"It took too long to connect to Github, time out!")
        print(e)
        sys.exit(1)

    print(latest_version_internet)
    logging.debug(f"Latest version of {software} on Github is {latest_version_internet}")
    return latest_version_internet

if __name__ == "__main__":
    get_latest_version_internet()