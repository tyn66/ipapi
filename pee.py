from peewee import MySQLDatabase, Model, CharField

# py_peewee连接的数据库名
db = MySQLDatabase('ip', host='127.0.0.1', user='root', passwd='123456', charset='utf8', port=3306)


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


class Ipprot(BaseModel):  # 继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
    ip = CharField(max_length=15)
    prot = CharField(max_length=6)



# 查询数据库是连接
print(db.is_closed())  # 返回false未连接
# 连接数据库
db.connect()
print(db.is_closed())  # 返回true表示已连接
# 创建table
Ipprot.create_table()

# 创建一条数据
p = Ipprot.create(ip='127.0.0.2', prot='7989')

#查询数据where后为查询条件
ps = Ipprot.select().where(Ipprot.prot=="7989")
print(ps)
for i in ps:
    print(i,i.ip,i.prot)

#修改数据库中的数据
s = Ipprot.get(ip='127.0.0.1')
s.prot = '999'
# 将修改后的数据进行存库
s.save()

