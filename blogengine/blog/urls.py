from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name = 'index'),
    path('mrsk/', mrks),
    path('sibur/', sibur),
    path('fromexel.html', work_exel),
    path('teleofis_state.html', tele_robot),
    path('swift.html', swift),
    path('teleofis_files.html', tele_file),
    path('beeline/', beeline),
    path('post1_iesk/', post1_iesk),
    path('post2_iesk/', post2_iesk),
    path('post3_iesk/', post3_iesk),
]
