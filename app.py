from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is a main page'


@app.route('/birthday')
def age():
    return '05.10.2008'


@app.route('/name')
def name():
    return 'Vlad'


@app.route('/hobi')
def my_hobi():
    return 'my hobi game'


if __name__ == '__main__':
    app.run(debug=True)
