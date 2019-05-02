from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name = 'index'),
    path('mrsk.html', mrks),
    path('sibur.html', sibur),
    path('teleofis_state.html', tele_robot),
    path('beeline.html', beeline),
    path('post1_iesk.html', post1_iesk),
    path('post2_iesk.html', post2_iesk),
    path('post3_iesk.html', post3_iesk),
]
