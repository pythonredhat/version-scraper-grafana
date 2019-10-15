import requests
import json
from bs4 import BeautifulSoup
from configparser import ConfigParser
from importlib import resources

def main():
    #get config
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("version_scraper_apache_kafka", "config.txt"))
    url = cfg.get("test", "url")

    kafkapage = requests.get(url)
    soup = BeautifulSoup(kafkapage,content, 'html.parser')

    kafka_release = soup.find_all('span')[1]

    print(kafka_release)

if __name__ == "__main__":
    main()





