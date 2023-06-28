from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

all_books = []
db = SQLAlchemy(app)


class books(db.Model):
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.FLOAT(), nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

# with app.app_context():
    # db.create_all()

@app.route('/')
def home():
    print(all_books)
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        all_books.append(data)
        print(all_books)
    return render_template("add.html")
