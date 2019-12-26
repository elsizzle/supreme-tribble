#!/usr/bin/python3 

import requests
response = requests.get('https://httpbin.org/ip')
print(format(response.json()['origin']))
