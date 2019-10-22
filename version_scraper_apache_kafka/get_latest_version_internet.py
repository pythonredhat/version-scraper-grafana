import requests
from bs4 import BeautifulSoup
from config import *

def get_latest_version_internet():
    kafka_page = requests.get(url_kafka)
    soup = BeautifulSoup(kafka_page.content, 'html.parser')

    kafka_release = soup.find_all('span')[0]

    latest_version_internet = kafka_release['id']

    print(latest_version_internet)
    return latest_version_internet

if __name__ == "__main__":
    get_latest_version_internet()