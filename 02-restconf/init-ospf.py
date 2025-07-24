#! /usr/bin/env python
import traceback
import json
import requests

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

url = "https://10.3.11.1/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf"

headers = {
    "Content-type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

auth = ('admin','admin')

try:
    response = requests.delete(url, headers=headers, auth=auth, verify=False)

    if response.status_code in [200,201,204]:
            print("Config delete success")

    else:
            print(f"Config delete failed with status code {response.status_code}")
            #print(vars(response))
            print(response.text)
except Exception as e:
    print(f"Exception occured: {e}")
    traceback.print_exc()
