from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=10,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    role=models.CharField(max_length=30,choices=[('member','Member'), ('admin','Admin')],default='member')
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    
