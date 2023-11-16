import os
from flask import Flask, render_template, request, send_file, redirect
from dotenv import load_dotenv
#from enumus import MAX_SCORE, NAME, students
#from models import *
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_BINDS'] = {
    'db': 'sqlite:///mydatabase1.db',
}
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'<Article {self.id}>'




@app.route("/")
def base():
    return render_template("base.html", title="Python course")


@app.route("/article", methods=['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(
            title=title,
            intro=intro,
            text=text
        )
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/article')
        except Exception as exs:
            return f'При збереженні запису виникла помилка: {exs}'
    else:
        return render_template('create_article.html')


@app.route("/articles")
def lsat_articles():
    articles = Article.query.order_by(Article.data.desc()).all()
    return render_template('articles.html', articles=articles)


@app.route("/articles/<int:id>/")
def article_detail(id):
    article = Article.query.get(id)
    return render_template("article_detail.html", article=article)


@app.route('/articles/<int:id>/delete')
def article_delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/article')
    except Exception as exc:
        return f'при видалені виникла помилка: {exc}'


@app.route('/articles/<int:id>/update', methods=['POST', 'GET'])
def article_update(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/article')
        except Exception as exc:
            return f'При оновленні запису виникла помилка: {exc}'
    else:
        return render_template("article_update.html", article=article)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
