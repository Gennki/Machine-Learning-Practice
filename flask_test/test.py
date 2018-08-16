from flask import Flask, request

app = Flask(__name__)


@app.route('/hello/')
def hello_world():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        key = request.args.get('key')
        return key
    elif request.method == 'POST':
        key = request.form['key']
        return key
