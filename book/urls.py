from django.contrib import admin
from django.urls import path,include
from book import views

urlpatterns = [
    path('add/',views.add_book,name='book-add'),
    path('view/',views.show_book,name='show-book'),
    path('update/<int:id>',views.update_books,name='update-books'),
    path('delete/<int:id>',views.delete_books,name='delete-books'),
    path('publication/add',views.add_publication,name='add-publication'),
    path('publication/view',views.display_publication,name='display-publication'),
    path('publication/update/<int:id>',views.edit_publication,name='edit-publication'),
    path('publication/delete/<int:id>',views.delete_publication,name='delete-publication')
]

