#! /usr/bin/env python
import unittest
import traceback
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = [
'''
<get-config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <source>
      <running/>
    </source>
    <filter>
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <router>
          <router-ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
            <ospf>
              <process-id>
                <id>1</id>
              </process-id>
            </ospf>
          </router-ospf>
        </router>
      </native>
    </filter>
  </get-config>
''',
]

with manager.connect(host='10.3.11.1',
                         port=830,
                         username='admin',
                         password='admin',
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        for rpc in payload:
            try:
                response = m.dispatch(et.fromstring(rpc))
                data = response.xml
            except RPCError as e:
                data = e.xml
                pass
            except Exception as e:
                traceback.print_exc()
                exit(1)

            # beautify output
            if et.iselement(data):
                data = et.tostring(data, pretty_print=True).decode()

            try:
                out = et.tostring(
                    et.fromstring(data.encode('utf-8')),
                    pretty_print=True
                ).decode()

                expected_output = '''
                <ospf>
                <process-id>
                  <id>1</id>
                  <network>
                    <ip>0.0.0.0</ip>
                    <wildcard>255.255.255.255</wildcard>
                    <area>0</area>
                  </network>
                  <passive-interface>
                    <interface>GigabitEthernet1.100</interface>
                    <interface>GigabitEthernet1.414</interface>
                  </passive-interface>
                </process-id>
                '''

                assert expected_output.replace(" ", "").replace("\n","") in out.replace(" ", "").replace("\n","") 

            except Exception as e:
                #traceback.print_exc()
                print("Test failed")
                exit(1)

print("Test passed")

