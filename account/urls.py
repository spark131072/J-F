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
    path('profile/',views.profile,name='profile'),
    path('upload_pic/',views.upload_pic,name='upload_pic')
    
]
