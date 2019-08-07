from django.db import models
from datetime import date
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
   
    def __str__(self):
        return '{} {}'.format(self.log_text, self.log_time)  

class telemetry(models.Model):

    vin = models.TextField(db_index= True)
    timetel = models.DateTimeField(default = timezone.now, auto_now_add=False)        
    cpu_temp = models.TextField(db_index= True)
    board_temp = models.TextField(db_index= True)

    def __str__(self):
        return '{} {}'.format(self.vin, self.timetel)  