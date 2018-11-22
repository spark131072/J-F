"""
131072
201118 - initial
account/urls.py



"""



# ============

from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
]
