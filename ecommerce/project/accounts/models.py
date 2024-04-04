from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
#class Accounts(models.Model):
 #   username = models.CharField(max_length=20)
  #  email = models.EmailField()
   # password = models.CharField(max_length=20)
    

class CustomUser(AbstractUser):
    name = models.CharField(null=True, max_length=100, blank=True)
