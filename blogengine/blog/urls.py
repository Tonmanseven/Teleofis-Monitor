from django.urls import path

from .views import *

urlpatterns = [
    path('index.html', posts_list),
    path('iesk.html', posts),
    path('fins.html', fins),
    path('sibur.html', sibur),
    path('teleofis_state.html', tele_robot),
    path('station_1.html', station_1),
    path('station_2.html', station_2),
    path('station_3.html', station_3),
    path('test.html', test),
]