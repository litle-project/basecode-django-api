# myapp/urls.py
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^list', views.index),
    re_path(r'^create', views.create),
    re_path(r'^detail/(?P<pk>\d+)/?$', views.detail),
    re_path(r'^update/(?P<pk>\d+)/?$', views.update),
    re_path(r'^delete/(?P<pk>\d+)/?$', views.delete),
]