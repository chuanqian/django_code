#coding:utf-8

from django.conf.urls import url
from django.urls import path
from .views import index

urlpatterns = [
	path("index/<str:name>/<int:age>", index)
]