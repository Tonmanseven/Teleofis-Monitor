from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name = 'index'),
    path('mrsk.html', mrks),
    path('sibur.html', sibur),
    path('teleofis_state.html', tele_robot),
<<<<<<< HEAD
    path('swift.html', swift),
=======
    path('teleofis_files.html', tele_file),
>>>>>>> 710dc9b40dc2c2dbf8fd7d5525b72669f1e8f08d
    path('beeline/', beeline),
    path('post1_iesk/', post1_iesk),
    path('post2_iesk/', post2_iesk),
    path('post3_iesk/', post3_iesk),
]
