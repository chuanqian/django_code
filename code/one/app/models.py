from django.db import models

# Create your models here.
class User(models.Model):
	user_id = models.IntegerField(max_length=10,verbose_name="自增唯一id",primary_key=True)
	name = models.CharField(max_length=20,verbose_name="姓名")
	age = models.IntegerField(max_length=3,verbose_name="年龄")
	info = models.CharField(max_length=100,verbose_name="自我介绍")

	class Meta:
		managed = True
		db_table = "User"
