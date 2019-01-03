"""
131072
201118 - initial
helloworld/view.py



"""


# =============

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
import random
from account.models import Geo, Taste
import requests
import json


# def geo_locate(request):
#
#     if request.user.is_authenticated:
#         _user = request.user
#
#         _lat = 0.000000
#         _lng = 0.000000
#
#         API_key = {'key': None}
#         API_key['key'] = getattr(settings, 'GOOGLE_MAPS_API_KEY', None)
#
#         if API_key['key'] is not None:
#             r = requests.post('https://www.googleapis.com/geolocation/v1/geolocate', params=API_key)
#
#             if r.status_code == requests.codes.ok:
#                 geo_info = json.loads(r.text)
#
#                 _lat = geo_info['location']['lat']
#                 _lng = geo_info['location']['lng']
#
#                 if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
#                     if Geo.objects.filter(user=_user).count() == 0:
#                         _username = request.user.username
#                         Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)
#
#                     else:
#                         current_user = Geo.objects.get(user=_user)
#                         current_user.lat = _lat
#                         current_user.lng = _lng
#                         current_user.save()

def geo_locate(request):

    if request.user.is_authenticated:
        _user = request.user

        _lat = 0.000000
        _lng = 0.000000

        if request.method == 'POST':
            geo_info = json.loads(request.body)

            _lat = geo_info['location']['lat']
            _lng = geo_info['location']['lng']

            if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
                if Geo.objects.filter(user=_user).count() == 0:
                    _username = request.user.username
                    Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)

                else:
                    current_user = Geo.objects.get(user=_user)
                    current_user.lat = _lat
                    current_user.lng = _lng
                    current_user.save()



def index(request):

    return render(request, 'index.html', locals())


def geo(request):

    geo_locate(request)

    return render(request, 'geo.html', locals())


def match(request):
    user_list = User.objects.all()
      
    info = [];
    for user in user_list:
        taste = Taste.objects.filter(user = user)
        item = {"name":user.username, 
                "self_attr":[taste.self_atc,
                         taste.self_amb,
                          taste.self_fun,
                          taste.self_int,
                          taste.self_sin]
                }; 
        info.append(item)

    obj = [
        {'user': 'A', 'device': 'deviceA', 'log': 'logA'},
        {'user': 'A', 'device': 'device1', 'log': 'ptrf1'},
        {'user': 'B', 'device': 'deviceb', 'log': 'ptrfb'},
    ]

    print(info);
    # test = [2, 4, 3, 5, 1];
    # test.sort();

    return render(request, 'match.html',locals())


def test(request):

    geo_locate(request)

    return render(request, 'test.html', locals())
