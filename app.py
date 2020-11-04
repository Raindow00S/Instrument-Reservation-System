from flask import Flask, render_template
from flask.globals import request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def child():
    if request.method == 'GET':
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug = True)
