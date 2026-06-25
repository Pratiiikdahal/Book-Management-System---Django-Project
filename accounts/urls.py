from django.urls import path
from accounts import views

urlpatterns=[
    path('signup/',views.register_user,name='register-user'),
    path('login/',views.login_user,name='login'),
]