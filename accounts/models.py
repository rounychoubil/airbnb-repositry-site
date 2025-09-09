from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    first_name= models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    e_mail= models.EmailField(max_length=254)