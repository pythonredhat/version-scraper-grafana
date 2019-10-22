import requests
import json
from bs4 import BeautifulSoup
from configparser import ConfigParser
from importlib import resources

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s", filename="./logs/test.log")


def main():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("version_scraper_apache_kafka", "config.txt"))
    url_kafka = cfg.get("test", "url_kafka")
    url_version_lord = cfg.get("test", "url_version_lord")

    kafka_page = requests.get(url_kafka)
    soup = BeautifulSoup(kafka_page.content, 'html.parser')

    kafka_release = soup.find_all('span')[0]

    kafka_release_version = kafka_release['id']

    version_lord_page = requests.get(url=url_version_lord)
    
    json_data = json.loads(version_lord_page.text)

    try:
        if json_data['current_version'] == kafka_release_version:
            print("All good in the hood!") 
        else:
            print("Version Lord is not up to date with RHEL site")
            data = {'current_version': kafka_release_version, 'software': 'Apache Kafka'}
            payload = requests.put(url=url_version_lord, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            logging.debug(payload.status_code)
            logging.debug(payload.content)
    except Exception as ex:
        logging.exception('caught an error')

if __name__ == "__main__":
    main()





