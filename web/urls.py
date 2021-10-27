# -*- coding:utf-8 -*- 

from django.urls import re_path
from web.consumers import WebConsumers
from web import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

websocket_url = [
    re_path(r'^ws/chat/(?P<room_name>[^/]+)/$', WebConsumers),
]