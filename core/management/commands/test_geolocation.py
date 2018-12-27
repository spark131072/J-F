from django.core.management.base import BaseCommand
from django.conf import settings
import requests
import json



def test_geolocation():

    API_key = {'key': None}
    API_key['key'] = getattr(settings, 'GOOGLE_MAPS_API_KEY', None)

    if API_key['key'] is not None:
        r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', params=API_key)

        print(r.status_code)

        if r.status_code == requests.codes.ok:
            print("OK")
            print(r.text)

            geo_info = json.loads(r.text)

            print(geo_info)
            print(geo_info['location']['lat'])
            print(geo_info['location']['lng'])

class Command(BaseCommand):
    help = 'test geolocation api'

    def handle(self, **options):
        test_geolocation()
