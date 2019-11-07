from .get_latest_version_internet import get_latest_version_internet
from .get_latest_version_versionlord import get_latest_version_versionlord
from .versionlord_updater import versionlord_updater
from .config import *

def main():

    latest_version_internet = get_latest_version_internet(url_github_api)
    
    latest_version_versionlord = get_latest_version_versionlord()

    versionlord_updater(latest_version_internet, latest_version_versionlord)

if __name__ == "__main__":
    main()





