#### 第三方ORM_sqlalchemy
##### 什么是sqlalchemy
SQLAlchemy是Python社区最知名的ORM工具之一，为搞笑和高性能对的数据库访问设计，实现了完整的企业级持久模型。
它可以搭配在任何一个python的web框架上，其中比较出名的是flask
##### sqlalchemy常用的基础模块
![sqlalchemy常用的基础模块](pictrue/sqlalchemy常用模块.png)
##### sqlalchemy常用类型
![sqlalchemy常用类型](pictrue/sqlalchemy常用类型.png)
##### sqlalchemy常用属性（列方法参数）
![sqlalchemy常用属性（列方法参数）](pictrue/sqlalchemy常用属性（列方法参数）.png)
##### 同步数据库方法
![同步数据库方法](pictrue/同步数据库方法.png)
##### 联系
数据库表结构更新模块：sqlalchemy-migrate alembic
自己联系配置
##### 整个过程
    1.下载依赖：sqlalchemy、pymysql
    2.创建数据库：create database sqlalchemy_test;
    3.sqlalchemy_test.py
```python
#coding:utf-8

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建模块
Base = declarative_base()
engine = create_engine("mysql+pymysql://root:123456@115.29.187.120/sqlalchemy_test")
db_session = sessionmaker(bind=engine)()

# 初始化
def init():
    Base.metadata.create_all(engine)

def drop():
    Base.metadata.drop_all()


class  User(Base):
    __tablename__ = "User"

    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(20),nullable=False)

if __name__ == '__main__':
    init()
```
    4.命令行窗口下运行：python sqlalchemy_test.py
    5.基本操作
```shell
>>> from sqlalchemy_test import User
>>> user = User(name="dater")
>>> from sqlalchemy_test import db_session
>>> db_session.add(user)
>>> db_session.commit()
>>> db_session.close()
>>> from sqlalchemy_test import db_session
>>> dates = db_session.query(User).filter_by(id=1)
>>> dates
<sqlalchemy.orm.query.Query object at 0x0000020898395970>
>>> dates = list(dates)
>>> dates
[<sqlalchemy_test.User object at 0x00000208985381F0>]
>>> dates = db_session.query(User).filter_by(id=1).one()
>>> dates.name
'dater'
```