from django.db import models
from datetime import date
from blog.views import decript
# Create your models here.

class Teleofis_state(models.Model):

    title = models.CharField(max_length = 150)
    timestamp = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(db_index=True)

    class Meta:
        db_table = '"{}"'.format(title)
        
    def __str__(self):
        return '{} {}'.format(self.timestamp, self.status)  
