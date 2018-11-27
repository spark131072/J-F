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


def index(request):

    return render(request, 'index.html', locals())

def geo(request):

    return render(request, 'geo.html', locals())
