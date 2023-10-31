import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/birthday')
def age():
    return '05.10.2008'


@app.route('/name')
def name():
    return 'Vlad'


@app.route('/hobby')
def my_hobby():
    return 'my hobby is a secret'


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))
