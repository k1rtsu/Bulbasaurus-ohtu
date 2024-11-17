from flask import redirect, render_template, request, jsonify, flash, url_for
from db_helper import reset_db
from config import app, test_env
from util import validate_book
import references as refs

def redirect_to_new_reference():
    return redirect(url_for("render_new"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new(error = None):
    return render_template("new_reference.html", error = error)

@app.route("/add_reference", methods=["POST"])
def add():
    if request.form.get("submit") == "book":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        try:
            validate_book(author, title, year, publisher)
            refs.add_book(author, title, year, publisher)
            return redirect("/references")
        except Exception as error:
            return new(error)

@app.route("/references")
def references():
    books = refs.get_all_books()
    total = len(books)
    return render_template("references.html", total = total, books = books)

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })