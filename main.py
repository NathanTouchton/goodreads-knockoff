from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

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

@app.route('/')
def home():
    # print(all_books)
    with app.app_context():
        result = db.session.execute(db.select(books).order_by("id"))
        all_books = result.scalars()
        return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }

        new_book = books(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()

    return render_template("add.html")
