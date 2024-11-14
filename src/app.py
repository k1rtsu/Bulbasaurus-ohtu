from flask import redirect, render_template, request, jsonify, flash
# from db_helper import reset_db
# from repositories.todo_repository import get_todos, create_todo, set_done
from config import app
# from util import validate_todo

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/references")
def references():
    return render_template("references.html")


# testausta varten oleva reitti
# if test_env:
#     @app.route("/reset_db")
#     def reset_database():
#         reset_db()
#         return jsonify({ 'message': "db reset" })