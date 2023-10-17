from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is a main page'


@app.route('birthday')
def main():
    return '05.10.2008'


@app.route('name')
def main():
    return 'Vlad'


if __name__ == '__main__':
    app.run(debug=True)
