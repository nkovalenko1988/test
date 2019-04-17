#!/usr/bin/python3
# -*- coding: utf-8 -*-


import urllib.request
import requests
import json

host = 'prod-ddf-service.scartel.dc:8080'
imsi = '250110201205100'


response = requests.get('http://' + host + '/spr/sm/getAllServices?subscriber_id=' + imsi)

#print(json.dumps(response.json(), sort_keys=True, indent=4))


parsed_string = json.loads(json.dumps(response.json()))


print(parsed_string['SERVICES'][2]['SERVICE_ID'])
