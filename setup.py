import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = ( HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="version-scraper-grafana",
    version="1.0.0",
    description="Version scraper for Grafana",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pythonredhat/version-scraper-grafana",
    author="Turbo Python",
    author_email="office@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["bs4", "json"],
    entry_points={
        "console_scripts": [
            "version_scraper_grafana=version_scraper_grafana.__main__:main",
        ]
    },
)
