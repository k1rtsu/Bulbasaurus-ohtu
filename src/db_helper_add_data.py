"""
Populate the database with example references.

Functions:
    add_data
    add_book
    add_article
    add_inproceedings
    add_misc
"""

from config import app
import references
import util


def add_data():
    """Add example data to the database"""
    add_book()
    add_article()
    add_inproceedings()
    add_misc()


def add_book():
    book = {
        "author": "Maija Pythonen",
        "title": "Pythonin alkeet",
        "year": "2009",
        "publisher": "Otava",
    }
    util.validate_book(book["author"], book["title"], book["year"], book["publisher"])
    references.add_book(book["author"], book["title"], book["year"], book["publisher"])


def add_article():
    article = {
        "author": "Hanna Javanen",
        "title": "Ketterän ohjelmistotuotannon tulevaisuus",
        "journal": "ATK-lehti",
        "volume": "4",
        "number": "2",
        "year": "2021",
        "pages_from": "89",
        "pages_to": "98",
        "doi": "10.1109/CVSM.2009.5071716",
        "url": "https://sisu.helsinki.fi",
    }
    util.validate_article(article)
    references.add_article(article)


def add_inproceedings():
    inproceedings = {
        "author": "Maik Schmidt",
        "title": "History-based merging of models",
        "year": "2009",
        "booktitle": "2009 ICSE Workshop on Comparison and Versioning of Software Models",
    }
    util.validate_inproceedings(
        inproceedings["author"],
        inproceedings["title"],
        inproceedings["year"],
        inproceedings["booktitle"],
    )
    references.add_inproceedings(
        inproceedings["author"],
        inproceedings["title"],
        inproceedings["year"],
        inproceedings["booktitle"],
    )


def add_misc():
    misc = {
        "author": "Kaija Sukanen",
        "title": "Olioperustainen ohjelmointi",
        "year": "1986",
        "note": "Laudaturtyö : Helsingin yliopisto, Tietojenkäsittelyopin laitos, 1986.",
    }
    util.validate_misc(misc["author"], misc["title"], misc["year"], misc["note"])
    references.add_misc(misc["author"], misc["title"], misc["year"], misc["note"])


if __name__ == "__main__":
    with app.app_context():
        add_data()
