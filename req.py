"""
131072
031218
test requests
"""


# =============

import requests
import json


API_key = {'key': 'AIzaSyD27byCiGJqgSBbiqpRwk-s69D5nl9oWEw'}
r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', params = API_key)

print(r.status_code)
if r.status_code == requests.codes.ok:
    print("OK")
    print(r.text)

    geo_info = json.loads(r.text)

    print(geo_info)
    print(geo_info['location']['lat'])
    print(geo_info['location']['lng'])
