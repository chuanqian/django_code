# coding:utf-8

from django.http import HttpResponse
from redis import Redis


def index(request, name, age):
    # name = request.GET.get("name","")
    # age = request.GET.get("age", 0)
    # cache = get_redis_connection("default")
    cache = Redis(host="115.29.187.120", port="6379", password="123456")
    cache.set("name", name, 20)
    cache.set("age", age, 20)
    print("name:{}".format(cache.get("name").decode("utf-8")))
    print("age:{}".format(cache.get("age").decode("utf-8")))
    return HttpResponse("hello, i am {0},age is {1}".format(cache.get("name").decode("utf-8"), cache.get("age").decode("utf-8")))


def testSlash(request):
    print("enter")
    return "111111"
