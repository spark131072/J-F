# chat/routing.py
from django.conf.urls import url

from . import consumers

channel_routing = {}

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]