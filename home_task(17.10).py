import os
from flask import Flask, render_template
from enumus import MAX_SCORE, NAME, students


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/birthday')
def birthday():
    return render_template('birthday.html', text='05.10.2008')


@app.route('/name')
def name():
    return render_template('name.html', text='Vlad')


@app.route('/hobby')
def my_hobby():
    return render_template('hobby.html', text='my hobby is a secret')


@app.route('/context')
def context():
    context_dict = {
        'title': 'Pyton Course',
        'name': NAME,
        'max_score': MAX_SCORE,
        'students': students
    }
    return render_template('context.html', **context_dict)


if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"))
