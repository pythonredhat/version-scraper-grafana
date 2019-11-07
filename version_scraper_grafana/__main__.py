from .get_latest_version_internet import connect_internet
from .get_latest_version_internet import parse_html
from .get_latest_version_versionlord import get_latest_version_versionlord
from .versionlord_updater import versionlord_updater
from .config import *

def main():

    kafka_page = connect_internet(url_kafka)

    latest_version_internet = parse_html(kafka_page)
    
    latest_version_versionlord = get_latest_version_versionlord()

    versionlord_updater(latest_version_internet, latest_version_versionlord)

if __name__ == "__main__":
    main()





