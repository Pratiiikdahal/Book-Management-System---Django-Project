from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=255,verbose_name='Author Name',default='Dummy')
    publication_name=models.CharField(max_length=255,verbose_name='Publication Name',null=True,blank=True)
    description=models.TextField(verbose_name='Author Description',null=True,blank=True)
    address=models.CharField(max_length=255,verbose_name='Author Address',null=True,blank=True)
    nationality=models.CharField(max_length=255,verbose_name='Nationality',null=True,blank=True)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    webiste=models.URLField()
    isActive=models.BooleanField(default=False)
    created_at=models.DateField(auto_now=True)
    modified_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    
