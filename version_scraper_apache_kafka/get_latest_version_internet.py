import requests
from bs4 import BeautifulSoup
from .config import *
import logging
import sys

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="./logs/scraper.log")

def get_latest_version_internet():

    try:
        kafka_page = requests.get(url_kafka)
    except requests.ConnectionError as e:
        logging.error(f"Unable to connect to the {software} website")
        logging.exception(e)
        print(f"Unable to connect to the {software} website")
        print(e)  
        sys.exit(1)
    except requests.Timeout as e:
        logging.error(f"It took too long to connect to the {software} website, time out!")
        logging.exception(e)
        print(f"It took too long to connect to the {software} website, time out!")
        print(e)
        sys.exit(1)

    try:
        soup = BeautifulSoup(kafka_page.content, 'html.parser')
        kafka_release = soup.find_all('span')[0]
        latest_version_internet = kafka_release['id']
    except TypeError as e:
        logging.error("Object data type is incorrect")
        logging.exception(e)
        print("Object data type is incorrect")
        print(e)
        sys.exit(1)
    except KeyError as e:
        logging.error("Attempting to scrape a key in dictionary that does not exist")
        logging.exception(e)
        print("Attempting to scrape a key in dictionary that does not exist")
        print(e)
        sys.exit(1)
    except AttributeError as e:
        logging.error("Attempting to access an invalid attribute of an object")
        logging.exception(e)
        print("Attempting to access an invalid attribute of an object")
        print(e)
        sys.exit(1)

    print(latest_version_internet)
    logging.debug(f"Latest version of {software} on the internet is {latest_version_internet}")
    return latest_version_internet

if __name__ == "__main__":
    get_latest_version_internet()