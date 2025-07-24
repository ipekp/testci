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

payload = {
    "process-id": [
        {
            "id": 1,
            "network": [
                {
                    "ip": "0.0.0.0",
                    "wildcard": "255.255.255.255",
                    "area": 0
                }
            ],
            "passive-interface": {
                "interface": [
                        "GigabitEthernet1.100",
                        "GigabitEthernet1.414",
                ]
            }
        }
    ]
}

try:
    response = requests.post(url, headers=headers, auth=auth, json=payload, verify=False)

    if response.status_code in [200,201]:
            print("Config application success")

    else:
            print(f"Config application failed with status code {response.status_code}")
            #print(vars(response))
            print(response.text)
except Exception as e:
    print(f"Exception occured: {e}")
    traceback.print_exc()
