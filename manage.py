#!/usr/bin/env python
import os
import sys
import requests
import json

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloworld.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def test_geolocation():

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
        print(geo_info['accuracy'])
