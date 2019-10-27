### Solution to running individual modules inside packages
```bash
#run the entire package
python -m version_scraper_apache_kafka
#run individual module
python -m version_scraper_apache_kafka.get_latest_version_internet
#run individual module
python -m version_scraper_apache_kafka.get_latest_version_versionlord
```

### Reference for running individual modules inside packages
```bash
https://stackoverflow.com/questions/45830856/running-a-module-in-a-package-importing-a-subpackage
```
