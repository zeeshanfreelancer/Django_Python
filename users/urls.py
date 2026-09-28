from django.urls import path
from .views import hello, profile

urlpatterns = [
    path("hello/", hello),
    path("profile/", profile),
]