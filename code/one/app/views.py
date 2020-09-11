#coding:utf-8

from django.http import HttpResponse

def index(request,name,age):
	# name = request.GET.get("name","")
	# age = request.GET.get("age", 0)
	return HttpResponse("hello, i am {0},age is {1}".format(name,age))