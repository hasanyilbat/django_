from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', student_page, name='student_page'),
    
]