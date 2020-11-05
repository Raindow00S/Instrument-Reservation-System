from flask import Flask, render_template
from flask.globals import request
from datetime import timedelta

# 用于输出运行日志
import logging
logging.basicConfig(level=logging.INFO, format='127.0.0.1 - - [%(asctime)s - %(name)s - %(levelname)s - %(message)s]')
logger = logging.getLogger(__name__)

app = Flask(__name__)
# 设置缓存时间为1秒
app.config['SENT_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)  # 好像没啥用啊……还是只能浏览器Ctrl+F5强制刷新
    
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def child():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 从html-js中的ajax-data字典提取数据
        user_name = request.form.get('user-name', default='user')
        password = request.form.get('password', default='pass')
        logger.info("登录用户："+str((user_name)+"密码："+str(password)))

        # TO DO 数据库相关代码



if __name__ == '__main__':
    app.run(debug = True)
