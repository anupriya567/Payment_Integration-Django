from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=500, default="")
    desc = models.CharField(max_length=5000, default="")
    email = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=15, default="")
    
    def __str__(self):
        return self.name