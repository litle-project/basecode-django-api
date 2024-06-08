# myapp/urls.py
from django.urls import path
from .views import Login, Logout

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view())
]