from django.db import models
from django.conf import settings
# Create your models here.


class Contactt(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    email = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=15, default="")
    
    def __str__(self):
        return self.name



class Paymentt(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)        

    def __str__(self):
        return self.name