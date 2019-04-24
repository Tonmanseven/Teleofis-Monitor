from django.db import models
from datetime import date
<<<<<<< HEAD
from blog.views import decript
# Create your models here.

class Teleofis_state(models.Model):

    title = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(db_index=True)

    class Meta:
        db_table = '"{}"'.format(title)
        
=======
from django.utils import timezone


class teleping(models.Model):
   
    host = models.CharField(max_length= 150, db_index= True, default = None)
    timestamp = models.DateTimeField(default = timezone.now, auto_now_add=False)
    inet = models.BooleanField(db_index=True)
    vpn = models.BooleanField(db_index=True)  

    def __str__(self):
        return '{} {} {} {}'.format(self.host, self.timestamp, self.inet, self.vpn)  

class telelog(models.Model):
   
    log_name = models.CharField(max_length= 150, db_index= True)
    log_text = models.TextField(db_index= True)
    log_time = models.DateTimeField(default = timezone.now, auto_now_add=False)
   
>>>>>>> origin
    def __str__(self):
        return '{} {}'.format(self.log_text, self.log_time)  

