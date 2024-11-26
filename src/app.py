from flask import (
    redirect,
    render_template,
    request,
    jsonify,
    url_for,
)
from db_helper import reset_db
from config import app, test_env
from util import validate_book, validate_article, validate_misc, validate_inproceedings
import references as refs


@app.route("/", methods=['GET', 'POST'])
def index(error = None):
    if request.method == 'POST':
        try:
            reference_type = request.form.get('submit')
            if reference_type == "inproceedings":
                handle_add_inproceedings()
            elif reference_type == 'book':
                handle_add_book()
            elif reference_type == 'misc':
                handle_add_misc()
            elif reference_type == 'article':
                handle_add_article()
        except Exception as e:
            error = e

    books = refs.get_all_books()
    articles = refs.get_all_articles()
    misc = refs.get_all_misc()
    inproceedings = refs.get_all_inproceedings()
    total = len(books)+len(articles)+len(misc)+len(inproceedings)

    return render_template("single_page_app.html", error=error, books=books, articles=articles, misc=misc, inproceedings=inproceedings, total=total)

@app.route("/remove_reference/<reference_id>", methods=["POST"])
def remove_reference(reference_id):
    refs.remove_reference(reference_id)
    return redirect('/')

def handle_add_book():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    try:
        validate_book(author, title, year, publisher)
        refs.add_book(author, title, year, publisher)
    except Exception as error: #pylint: disable=broad-exception-caught
        raise error
        
def handle_add_misc():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    note = request.form["note"]
    try:
        # a bug in here, check the function parameters
        validate_misc(author, title, year, note)
        refs.add_misc(author, title, year, note)
    except Exception as error: #pylint: disable=broad-exception-caught
        raise error
        
def handle_add_article():
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
    except Exception as error: #pylint: disable=broad-exception-caught
        raise error
        
def handle_add_inproceedings():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    booktitle = request.form["booktitle"]
    try:
        validate_inproceedings(author, title, year, booktitle)
        refs.add_inproceedings(author, title, year, booktitle)
    except Exception as error: #pylint: disable=broad-exception-caught
        raise error

if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
