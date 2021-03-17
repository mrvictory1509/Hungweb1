from django.urls import path, include
from .import views 

urlpatterns = [
    path('', views.login),
    path('login_user', views.login_user),
]