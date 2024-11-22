from django.urls import path
from myapp.views import *

urlpatterns = [
    path("hello/", HelloWorld),
]