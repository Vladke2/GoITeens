import os
from app import app
from dotenv import load_dotenv
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
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



