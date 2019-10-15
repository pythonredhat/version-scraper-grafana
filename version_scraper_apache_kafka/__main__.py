import requests
import json
from configparser import ConfigParser
from importlib import resources

def main():
    #get config
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("hello_world_app", "config.txt"))
    url = cfg.get("test", "url")
    
    #test code
    response = requests.get(url=url)
    print (response.status_code)
    print (response.content)
    json_data = json.loads(response.text)
    github_latest_version = (json_data["name"])
    print(f"Latest version on Github is {github_latest_version}")

if __name__ == "__main__":
    main()





