from flask import redirect, render_template, request, jsonify, flash, url_for #pylint: disable=unused-import
from db_helper import reset_db
from config import app, test_env
from util import validate_book, validate_article, validate_misc, validate_inproceedings
import references as refs

def redirect_to_new_reference():
    return redirect(url_for("render_new"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new_book_reference")
def new_book(error = None):
    return render_template("new_book_reference.html", error = error)

@app.route("/new_article_reference")
def new_article(error = None):
    return render_template("new_article_reference.html", error = error)

@app.route("/new_misc_reference")
def new_misc(error=None):
    return render_template("new_misc_reference.html", error=error)

@app.route("/new_inproceedings_reference")
def new_inproceedings(error = None):
    return render_template("new_inproceedings_reference.html", error = error)

@app.route("/add_reference", methods=["POST"])
def add(): #pylint: disable=inconsistent-return-statements
    if request.form.get("submit") == "book":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        publisher = request.form["publisher"]
        try:
            validate_book(author, title, year, publisher)
            refs.add_book(author, title, year, publisher)
            return redirect("/references")
        except Exception as error: #pylint: disable=broad-exception-caught
            return new_book(error)
    if request.form.get("submit") == "article":
        author = request.form["author"]
        title = request.form["title"]
        journal = request.form["journal"]
        volume = request.form["volume"]
        number = request.form["number"]
        year = request.form["year"]
        pages_from = request.form["pages_from"]
        pages_to = request.form["pages_to"]
        doi = request.form["doi"]
        url = request.form["url"]
        article_data = {
                "author": author,
                "title": title,
                "journal": journal,
                "volume": volume,
                "number": number,
                "year": year,
                "pages_from": pages_from,
                "pages_to": pages_to,
                "doi": doi,
                "url": url
        }
        try:
            validate_article(article_data)
            refs.add_article(article_data)
            return redirect("/references")
        except Exception as error: #pylint: disable=broad-exception-caught
            return new_article(error)
    if request.form.get("submit") == "misc":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        note = request.form["note"]
        try:
            validate_misc(author, title, year, note)
            refs.add_book(author, title, year, note)
            return redirect("/references")
        except Exception as error: #pylint: disable=broad-exception-caught
            return new_misc(error)
    if request.form.get("submit") == "inproceedings":
        author = request.form["author"]
        title = request.form["title"]
        year = request.form["year"]
        booktitle = request.form["booktitle"]
        try:
            validate_inproceedings(author, title, year, booktitle)
            refs.add_inproceedings(author, title, year, booktitle)
            return redirect("/references")
        except Exception as error: #pylint: disable=broad-exception-caught
            return new_inproceedings(error)

@app.route("/references")
def references():
    books = refs.get_all_books()
    articles = refs.get_all_articles()
    miscs = refs.get_all_misc()
    inproceedings = refs.get_all_inproceedings()
    total = len(books)+len(articles)+len(miscs)+len(inproceedings)
    return render_template("references.html", 
                           total = total, 
                           books = books, 
                           articles = articles,
                           miscs = miscs,
                           inproceedings = inproceedings)

@app.route("/remove_reference/<reference_id>", methods=["POST"])
def remove_reference(reference_id):
    refs.remove_reference(reference_id)
    books = refs.get_all_books()
    articles = refs.get_all_articles()
    miscs = refs.get_all_misc()
    inproceedings = refs.get_all_inproceedings()
    total = len(books)+len(articles)+len(miscs)+len(inproceedings)
    return render_template("references.html", 
                           total = total, 
                           books = books, 
                           articles = articles,
                           miscs = miscs,
                           inproceedings = inproceedings)

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
