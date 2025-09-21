from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(100), unique = True, nullable = False)
    publisher = db.Column(db.String(80), unique = True, nullable = False)

    def __repr__(self):
        return f"{self.title} - {self.author} - {self.publisher}"

@app.route('/book')
def get_book():
    return {"book": "book data"}