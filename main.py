import os
import re
import json
import requests

REPO_NAME = os.getenv("REPO_NAME", "adoptium/temurin8-binaries")
repatter = re.compile(r"OpenJDK8U-jre_x64_windows_hotspot_[0-9a-z]*.zip")

url = f"https://api.github.com/repos/{REPO_NAME}/releases/latest"
response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"}).json()

for v in response["assets"]:
    if(repatter.match(v["name"])):
        print(json.dumps(v))
        break