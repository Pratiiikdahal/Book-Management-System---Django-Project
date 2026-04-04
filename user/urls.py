from django.urls import path,include
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name='user/login.html'),name='login'),
]
