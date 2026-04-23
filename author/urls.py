from django.urls import path,include
from author import views

urlpatterns=[
    path('add-author/',views.add_author,name='add-author'),
    path('display-author/',views.author_display,name='display-author'),
   # path('update-author/<int:id>',views.update_author,name='update-author'),
]