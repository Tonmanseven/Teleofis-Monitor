from django.db import models
from datetime import date


class Teleofis(models.Model):
   
    host = models.CharField(max_length= 150, db_index= True, default = None)
    timestamp = models.DateTimeField(auto_now_add=False)
    status = models.BooleanField(db_index=True)  

    class Meta:
        db_table = '"teleofis_state"'      

    def __str__(self):
        return '{}'.format(self.status)  

