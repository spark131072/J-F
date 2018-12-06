from django.core.management.base import BaseCommand
from django.conf import settings
import requests
import json



def test_geocoding():

    API_key = {'key': None}
    API_key['key'] = getattr(settings, 'GOOGLE_MAPS_API_KEY', None)

    if API_key['key'] is not None:
        r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', params=API_key)

        print(r.status_code)

        if r.status_code == requests.codes.ok:
            print(r.text)

            geo_info = json.loads(r.text)
            latlng = str(geo_info['location']['lat']) + "," + str(geo_info['location']['lng'])

            para = {}
            para['latlng'] = latlng
            para['key'] = API_key['key']

            re = requests.post('https://maps.googleapis.com/maps/api/geocode/json', params=para)

            print(re.status_code)

            if re.status_code == requests.codes.ok:
                address_info = json.loads(re.text)

                # print(address_info)
                print(type(address_info['results'][0]))
                print(address_info['results'][0]['formatted_address'])
                print(address_info['results'][0]['place_id'])



class Command(BaseCommand):
    help = 'test geolocation api'

    def handle(self, **options):
        test_geocoding()
