from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Author)
class authorAdmin(admin.ModelAdmin):
    list_display=['publication_name','description','address','nationality','email',
                  'phone','webiste','isActive','created_at','modified_by']
    