#### Djanog整合redis
##### 什么是redis
    1.Redis是一个基于内存的非关系型数据库。它通过key：value的形式存储。有着多种数据结构，如字符串，列表，集合等
    2.通过redis我们可以进行数据缓存，防止底层数据库频繁io，提升性能
##### redis的依赖
    1.pip install redis
    2.pip install django-redis
##### django中redis的配置方法
![django中redis的配置方法](pictrue/django中redis的配置方法.png)
##### 不依赖django的redis配置方法
![不依赖django的redis配置方法](pictrue/不依赖django的redis配置方法.png)
##### Django中使用redis的方法
```python
#coding:utf-8

from django.http import HttpResponse
from django_redis import get_redis_connection
from redis import Redis

def index(request,name,age):
	# name = request.GET.get("name","")
	# age = request.GET.get("age", 0)
    cache = get_redis_connection("default")
    cache.set("name",name,20)
    cache.set("age",age,20)
    print("name:{}".format(cache.get("name")))
    print("age:{}".format(cache.get("age")))
    return HttpResponse("hello, i am {0},age is {1}".format(cache.get("name"),cache.get("age")))
```
##### 不依赖Django使用Redis的方法
```python
#coding:utf-8

from django.http import HttpResponse
from django_redis import get_redis_connection
from redis import Redis

def index(request,name,age):
	# name = request.GET.get("name","")
	# age = request.GET.get("age", 0)
    # cache = get_redis_connection("default")
    cache = Redis(host="115.29.187.120",port="6379",password="123456")
    cache.set("name",name,20)
    cache.set("age",age,20)
    print("name:{}".format(cache.get("name")))
    print("age:{}".format(cache.get("age")))
    return HttpResponse("hello, i am {0},age is {1}".format(cache.get("name"),cache.get("age")))
```