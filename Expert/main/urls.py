from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main"),
    path('dop/', index2, name="dop")
]
