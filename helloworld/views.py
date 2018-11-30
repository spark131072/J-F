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
import random
from account.models import Geo
import requests
import json


def index(request):

    return render(request, 'index.html', locals())


def geo(request):

    if request.user.is_authenticated:
        _user = request.user

        _lat = 0.000000
        _lng = 0.000000

        if request.method == 'POST':
            _lat = request.POST.get('lat')
            # json_receive = json.loads(request.body)

            # _lat = json_receive.lat
            # _lng = json_receive['lng']

            print(_lat)

        if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
            if Geo.objects.filter(user=_user).count() == 0:
                _username = request.user.username
                Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)

            else:
                current_user = Geo.objects.get(user=_user)
                current_user.lat = _lat
                current_user.lng = _lng
                current_user.save()

    return render(request, 'geo.html', locals())

def weather(request):

    if request.user.is_authenticated:
        _user = request.user

        _lat = 0.000000
        _lng = 0.000000

        if request.method == 'POST':
            _lat = request.POST.get('lat')
            _lng = request.POST.get('lng')

        print(_lat, _lng)

        if _lat != 0.000000 and _lng != 0.000000 and _lat is not None and _lng is not None:
            if Geo.objects.filter(user=_user).count() == 0:
                _username = request.user.username
                Geo.objects.create(lat=_lat, lng=_lng, username=_username, user=_user)

            else:
                current_user = Geo.objects.get(user=_user)
                current_user.lat = _lat
                current_user.lng = _lng
                current_user.save()

    return render(request, 'weather.html', locals())

def match(request):

    return render(request, 'match.html', locals())
