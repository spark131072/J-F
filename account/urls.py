"""
131072
201118 - initial
account/urls.py



"""



# ============

from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
