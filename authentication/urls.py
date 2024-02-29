from django.shortcuts import redirect
from django.urls import path, include

from . import views

urlpatterns = [
    path('login', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

]