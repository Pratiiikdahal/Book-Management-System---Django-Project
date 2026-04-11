from django.db import models
from author.models import Author

# Create your models here.
class Publication(models.Model):
    publication_name=models.CharField(max_length=255,verbose_name='Publication Name',null=True,blank=True)
    address=models.CharField(max_length=255,verbose_name='Publication Address',null=True,blank=True)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    webiste=models.URLField()
    isActive=models.BooleanField(default=False)
    created_at=models.DateField(auto_now=True)
    
    def __str__(self) ->str:
        return self.publication_name
    
class Category(models.Model):
    category_name=models.CharField(max_length=255,null=True,blank=True,verbose_name='Category Name')
    created_at=models.DateField(auto_now=True)
    modified_at=models.DateField(auto_now_add=True)
    
    def __str__(self) ->str:
        return self.category_name
    
class Genre(models.Model):
    genre_name=models.CharField(max_length=255,null=True,blank=True)
    isActive=models.BooleanField(default=False)
    created_at=models.DateField(auto_now=True)
    
    def __str__(self) ->str:
        return self.genre_name
    
class Book(models.Model):
    book_name=models.CharField(verbose_name='Book Name',max_length=255,null=True,blank=True)
    file=models.FileField(upload_to='book/',null=True,blank=True)
    image=models.ImageField(upload_to='book_image',null=True,blank=True)
    publication=models.ForeignKey(Publication,on_delete=models.RESTRICT)
    category=models.ManyToManyField(Category)
    genre=models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
    author=models.ManyToManyField(Author)
    edition=models.PositiveIntegerField()
    isbn=models.CharField(max_length=255,null=True,blank=True,unique=True)
    page_number=models.PositiveIntegerField()
    description=models.TextField()
    demo_text=models.CharField(max_length=50,null=True,blank=True)
    price=models.DecimalField(max_digits=100,decimal_places=2)
    language=models.CharField(max_length=255,null=True,blank=True)
    discount_percentage=models.DecimalField(max_digits=100,decimal_places=2)
    isActive=models.BooleanField()
    isPublished=models.BooleanField()
    created_at=models.DateField(auto_now=True)
    modified_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name