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

### coverage.py commands
```bash
#run coverage on multiple modules
coverage run -m unittest discover
#get the report
coverage report -m
#produce the html report, this will create an html folder in the directory, in there open index.html in browser
coverage html
```

### how to setup Mock for testing external APIs:
```bash
https://stackoverflow.com/questions/50157543/unittest-django-mock-external-api-what-is-proper-way
```