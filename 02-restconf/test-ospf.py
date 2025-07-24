#! /usr/bin/env python
import traceback
import json
import requests
import unittest

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

url = "https://10.3.11.1/restconf/data/Cisco-IOS-XE-native:native/router/router-ospf/ospf/process-id=1"

headers = {
    "Content-type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

auth = ('admin','admin')

expected_response = {
        "Cisco-IOS-XE-ospf:process-id": {
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
}

try:
    response = requests.get(url, headers=headers, auth=auth, verify=False)

    if response.status_code == 200:
            print("Config retrieve success")
            print(json.dumps(response.json(),indent=4))

    else:
            print(f"Config retrieve failed with status code {response.status_code}")
            #print(vars(response))
            print(response.text)

    # unit test
    assert response.json() == expected_response, "Expected response is different from running-config"
    
except Exception as e:
    print(f"Test failed: {e}")
    traceback.print_exc()
    print(json.dumps(response.json(),indent=4))
    print(json.dumps(expected_response,indent=4))
    exit(1)

print("Test passed")
