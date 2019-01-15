from peewee import MySQLDatabase, Model, CharField

# py_peewee连接的数据库名
db = MySQLDatabase('ip', host='127.0.0.1', user='root', passwd='123456', charset='utf8', port=3306)


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


class Ipport(BaseModel):  # 继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
    Servernumber = CharField(max_length=10)#服务器编号
    ip = CharField(max_length=15)#ip地址
    port = CharField(max_length=6)#端口号
    inserttime = CharField(max_length=255)#插入时间
    opentime = CharField(max_length=255)#修改时间


# TODO 创建table
try:
    Ipport.create_table()
except Ellipsis as e:
    print(e)
