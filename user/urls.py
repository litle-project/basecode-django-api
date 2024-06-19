# myapp/urls.py
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('list', views.index)
]