from flask import Flask,request
from utils import utils
import time
app = Flask(__name__)


@app.route('/',methods=["POST"])
def hello_world():
    ip = request.form.get('ip')
    Servernumber = request.form.get('Servernumber')
    port = request.form.get('port')
    inserttime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    opentime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    ps = utils.Ipport.select().where(utils.Ipport.Servernumber == Servernumber)
    for i in ps:
        s = i.Servernumber
        if s == Servernumber:
            ss = utils.Ipport.get(Servernumber=Servernumber)
            ss.ip = ip
            ss.opentime=opentime
            # 将修改后的数据进行存库
            ss.save()
            return "保存成功"
    utils.Ipport.create(ip=ip, port=port, inserttime=inserttime, opentime=opentime, Servernumber=Servernumber)
    return '保存成功!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7988)
