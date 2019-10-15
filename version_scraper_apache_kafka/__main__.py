import requests
import json
from bs4 import BeautifulSoup
from configparser import ConfigParser
from importlib import resources

def main():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("version_scraper_apache_kafka", "config.txt"))
    url_kafka = cfg.get("test", "url_kafka")
    url_version_lord = cfg.get("test", "url_version_lord")

    kafka_page = requests.get(url_kafka)
    soup = BeautifulSoup(kafka_page.content, 'html.parser')

    kafka_release = soup.find_all('span')[0]

    print(kafka_release['id'])

    version_lord_page = requests.get(url=url_version_lord)
    
    json_data = json.loads(version_lord_page.text)

    print(json_data)


if __name__ == "__main__":
    main()





