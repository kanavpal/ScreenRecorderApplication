from django.contrib import admin
from django.urls import path
from SSApp import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('signup',views.signup,name='Signup'),
]