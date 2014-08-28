__author__ = 'rushil'
import requests
from pprint import pprint

response = requests.get('http://placekitten.com/')

# Add your code below!
print(response.status_code)
pprint(response.headers)