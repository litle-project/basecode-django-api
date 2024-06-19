# myapp/urls.py
from django.urls import re_path
from .views import Login, Logout

urlpatterns = [
    re_path('login', Login.as_view()),
    re_path('logout', Logout.as_view())
]