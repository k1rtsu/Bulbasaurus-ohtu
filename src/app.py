from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
# from repositories.todo_repository import get_todos, create_todo, set_done
from config import app, test_env
# from util import validate_todo
import references as refs

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/add_reference", methods=["POST"])
def add():
    if request.form.get("submit") == "book":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        refs.add_book(author, title, year, publisher)
    return redirect("/references")

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