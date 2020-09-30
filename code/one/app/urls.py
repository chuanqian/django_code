# coding:utf-8

from django.urls import path
from .views import index, testSlash

urlpatterns = [
    path("index/<str:name>/<int:age>", index),
    path("test/", testSlash)
]
