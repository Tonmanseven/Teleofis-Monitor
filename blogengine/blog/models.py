from django.db import models
from datetime import date
# Create your models here.

class Teleofis_state(models.Model):
    
    timestamp = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(db_index=True)

    class Meta:
        db_table = '"teleofis_state"'
        
    def __str__(self):
        return '{} {}'.format(self.timestamp, self.status)  
