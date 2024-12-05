from flask import (
    redirect,
    render_template,
    request,
    jsonify,
)
from db_helper import reset_db
from config import app, test_env
from util import (
    validate_book,
    validate_article,
    validate_misc,
    validate_inproceedings,
    validate_edit,
    validate_search,
    filter_items,
    UserInputError
)
import references as refs
import get_references
import edit_references

@app.route("/", methods=['GET', 'POST'])
def index(error = None):
    selected_option = 'book' # default value

    if request.method == 'POST':
        try:
            selected_option = request.form.get('selected-option')
            reference_type = request.form.get('submit')
            if reference_type == "inproceedings":
                handle_add_inproceedings()
            elif reference_type == 'book':
                handle_add_book()
            elif reference_type == 'misc':
                handle_add_misc()
            elif reference_type == 'article':
                handle_add_article()
        except UserInputError as e:
            error = e

    books, articles, misc, inproceedings = get_all_references()
    total = len(books)+len(articles)+len(misc)+len(inproceedings)

    return render_template("single_page_app.html",
                           error=error,
                           books=books,
                           articles=articles,
                           misc=misc,
                           inproceedings=inproceedings,
                           total=total,
                           selected_option=selected_option)

@app.route("/edit_reference", methods=["POST"])
def edit_reference():
    reference_id = request.form.get("reference_id")
    if not get_references.reference_exists(reference_id):
        return redirect("/")

    form_data = request.form.to_dict()
    reference_type = form_data["reference_type"]
    del form_data["button"]
    del form_data["reference_id"]
    del form_data["reference_type"]

    cleaned_data = {}
    for key, value in form_data.items():
        cleaned_data[key[5:]] = value

    try:
        validate_edit(cleaned_data, reference_type)
        edit_references.update_reference(cleaned_data, reference_id)
        return redirect("/")
    except UserInputError as err:
        error = err # should the error be used?
        books, articles, misc, inproceedings = get_all_references()
        total = len(books)+len(articles)+len(misc)+len(inproceedings)

        return render_template("single_page_app.html",
                            error=error,
                            books=books,
                            articles=articles,
                            misc=misc,
                            inproceedings=inproceedings,
                            total=total)

@app.route("/remove_reference/<reference_id>", methods=["POST"])
def remove_reference(reference_id):
    refs.remove_reference(reference_id)
    return redirect('/')

@app.route("/search", methods=['POST'])
def basic_search(error = None):
    submit_type = request.form.get('submit')

    if submit_type == "clear":
        return redirect('/')

    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    year_from = request.form["year_from"]
    year_to = request.form["year_to"]
    reference_type = request.form["reference_type"]
    search_data = {
        "author": author,
        "title": title,
        "year": year,
        "year_from": year_from,
        "year_to": year_to,
        "reference_type": reference_type,
    }
    try:
        validate_search(search_data)
    except UserInputError as e:
        error = e
    books, articles, misc, inproceedings = get_all_references()

    books = filter_items(books, 'books', 'book_info', search_data)
    articles = filter_items(articles, 'articles', 'article_info', search_data)
    misc = filter_items(misc, 'misc', 'misc_info', search_data)
    inproceedings = filter_items(inproceedings, 'inproceedings', 'inproceedings_info', search_data)
    total = len(books) + len(articles) + len(misc) + len(inproceedings)
    return render_template("single_page_app.html",
                            error=error,
                            books=books,
                            articles=articles,
                            misc=misc,
                            inproceedings=inproceedings,
                            total=total)

def handle_add_book():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    publisher = request.form["publisher"]
    try:
        validate_book(author, title, year, publisher)
        refs.add_book(author, title, year, publisher)
    except UserInputError as error: #pylint: disable=broad-exception-caught
        raise error

def get_all_references():
    books = refs.get_all_books()
    articles = refs.get_all_articles()
    misc = refs.get_all_misc()
    inproceedings = refs.get_all_inproceedings()
    return books, articles, misc, inproceedings

def handle_add_misc():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    note = request.form["note"]
    try:
        validate_misc(author, title, year, note)
        refs.add_misc(author, title, year, note)
    except UserInputError as error: #pylint: disable=broad-exception-caught
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
    except UserInputError as error: #pylint: disable=broad-exception-caught
        raise error

def handle_add_inproceedings():
    author = request.form["author"]
    title = request.form["title"]
    year = request.form["year"]
    booktitle = request.form["booktitle"]
    try:
        validate_inproceedings(author, title, year, booktitle)
        refs.add_inproceedings(author, title, year, booktitle)
    except UserInputError as error: #pylint: disable=broad-exception-caught
        raise error

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
