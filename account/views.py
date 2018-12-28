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
from account.models import Taste


def taste(request, object):

    if request.user.is_authenticated:
        _user = request.user

        _self_atc = 0.0
        _self_amb = 0.0
        _self_fun = 0.0
        _self_int = 0.0
        _self_sin = 0.0
        _prtn_atc = 0.0
        _prtn_amb = 0.0
        _prtn_fun = 0.0
        _prtn_int = 0.0
        _prtn_sin = 0.0

        if request.method == 'POST':
            taste_data = json.loads(request.body)

            if len(taste_data) == 5 and taste_data is not None:
                fin = 0

                if object == 'self':
                    fin = 1
                    _self_atc = taste_data[0]['value']
                    _self_amb = taste_data[4]['value']
                    _self_fun = taste_data[3]['value']
                    _self_int = taste_data[2]['value']
                    _self_sin = taste_data[1]['value']

                elif object == 'prtn':
                    fin = 1
                    _prtn_atc = taste_data[0]['value']
                    _prtn_amb = taste_data[4]['value']
                    _prtn_fun = taste_data[3]['value']
                    _prtn_int = taste_data[2]['value']
                    _prtn_sin = taste_data[1]['value']

                if fin == 1:
                    if Taste.objects.filter(user=_user).count() == 0:
                        _username = request.user.username
                        Taste.objects.create(self_atc = _self_atc, self_amb = _self_amb, self_fun = _self_fun, self_int = _self_int, self_sin = _self_sin, \
                                             prtn_atc = _prtn_atc, prtn_amb = _prtn_amb, prtn_fun = _prtn_fun, prtn_int = _prtn_int, prtn_sin = _prtn_sin, \
                                             username=_username, user=_user)

                    else:
                        current_user = Taste.objects.get(user=_user)

                        if object == 'self':
                            current_user.self_atc = _self_atc
                            current_user.self_amb = _self_amb
                            current_user.self_fun = _self_fun
                            current_user.self_int = _self_int
                            current_user.self_sin = _self_sin

                        elif object =='prtn':
                            current_user.prtn_atc = _prtn_atc
                            current_user.prtn_amb = _prtn_amb
                            current_user.prtn_fun = _prtn_fun
                            current_user.prtn_int = _prtn_int
                            current_user.prtn_sin = _prtn_sin

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

    taste(request, "self")
    return render(request,'chart-self.html',locals())

def chart_partner(request):

    taste(request, "prtn")

    if request.method == 'POST':
        data = json.loads(request.body)
        print(len(data))
        print(data[0]['axis'], data[0]['value'])
        print(data[1]['axis'], data[1]['value'])
        print(data[2]['axis'], data[2]['value'])
        print(data[3]['axis'], data[3]['value'])
        print(data[4]['axis'], data[4]['value'])


    return render(request,'chart-partner.html',locals())
