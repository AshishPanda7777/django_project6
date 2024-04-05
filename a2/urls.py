from django.urls import path
from a2.views import *
app_name='anything'
urlpatterns = [
    path('name/',name,name='name')
]