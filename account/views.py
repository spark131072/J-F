"""
131072
201118 - initial
account/views.py



"""


# =============

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ImageUploadForm
from django.http import HttpResponse
import json


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

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.gender = form.cleaned_data.get('gender')
            user.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def profile(request):
    return render(request,'profile.html',locals())


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            user.profile.image = form.cleaned_data['image']
            user.save()
            return redirect('profile')
    return HttpResponseForbidden('allowed only via POST')

def chart_self(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        print(type(data[0]))
        print(data[0]['axis'], data[0]['value'])
        print(data[1]['axis'], data[1]['value'])
        print(data[2]['axis'], data[2]['value'])
        print(data[3]['axis'], data[3]['value'])
        print(data[4]['axis'], data[4]['value'])

    return render(request,'chart-self.html',locals())

def chart_partner(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        print(type(data[0]))
        print(data[0]['axis'], data[0]['value'])
        print(data[1]['axis'], data[1]['value'])
        print(data[2]['axis'], data[2]['value'])
        print(data[3]['axis'], data[3]['value'])
        print(data[4]['axis'], data[4]['value'])


    return render(request,'chart-partner.html',locals())

def test(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        print(type(data[0]))
        print(data[0]['axis'], data[0]['value'])
        print(data[1]['axis'], data[1]['value'])
        print(data[2]['axis'], data[2]['value'])
        print(data[3]['axis'], data[3]['value'])
        print(data[4]['axis'], data[4]['value'])
    return render(request, 'testing.html', locals())
