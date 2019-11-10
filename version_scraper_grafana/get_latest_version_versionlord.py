import requests
from .config import *
import json

def get_latest_version_versionlord():

    version_lord_page = requests.get(url=url_version_lord)
    
    json_data = json.loads(version_lord_page.text)

    latest_version_versionlord = json_data['current_version']

    print(latest_version_versionlord)
    return latest_version_versionlord

if __name__ == "__main__":
    get_latest_version_versionlord()