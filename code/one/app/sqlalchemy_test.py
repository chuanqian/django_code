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
        

