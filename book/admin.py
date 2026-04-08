from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display=['publication_name','address','email','phone','webiste','isActive','created_at']
    list_per_page=30
    
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['category_name','created_at','modified_at']
    
@admin.register(Genre)
class genreAdmin(admin.ModelAdmin):
    list_display=['genre_name','isActive','created_at']
    
@admin.register(Book)
class bookAdmin(admin.ModelAdmin):
    list_display=['book_name','file','image','publication','genre','edition','isbn','page_number','description',
                  'demo_text','price','language','discount_percentage','isActive','isPublished','created_at','modified_at']
    

    
    
