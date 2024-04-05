from django.contrib import admin
from django.urls import path
from a1.views import *
app_name='anything'
urlpatterns = [
    path('ph/',ph,name='ph')
]
