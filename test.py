from utils import utils
import time
ip = "127.0.0.1"
prot = "7888"
inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
opentime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
ps = utils.Ipprot.select().where(utils.Ipprot.prot == prot)
for i in ps:
    s = i.prot
    print(s)
    if s == prot:
        ss = utils.Ipprot.get(prot = prot)
        ss.ip = '192.168.50.46'
        # 将修改后的数据进行存库
        ss.save()
utils.Ipprot.create(ip=ip, prot=prot, inserttime=inserttime, opentime=opentime)
