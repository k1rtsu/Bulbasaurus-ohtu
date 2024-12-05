"""
Populate the database with example references.

Functions:

    add_data

    loop
    
    add_book

    add_article

    add_inproceedings

    add_misc
"""

from random import randint, shuffle
from config import app
import references
import util


FIRST_NAMES = [
    "Maija",
    "Kaija",
    "Hanna",
    "Yrjö",
    "Hannu",
    "Matti",
    "Johannes",
    "Pirjo",
    "Otto",
    "Kaapo",
    "Hemuli",
    "Nyyrikki",
    "Kyllikki",
]
LAST_NAMES = [
    "Pythonen",
    "Javanen",
    "Ruoste",
    "Turing",
    "Pascal",
    "Luokkanen",
    "Zuse",
    "Ohjelmoija",
    "Metodi",
    "Buginen",
    "Listanen",
    "Tietonen",
    "Bombe",
    "Enigma",
]


def add_data():
    """Add example data to the database"""
    loop(add_book)
    loop(add_article)
    loop(add_inproceedings)
    loop(add_misc)


def loop(add_function):
    shuffle(FIRST_NAMES)
    shuffle(LAST_NAMES)
    for i in range(2):
        first = FIRST_NAMES[i]
        last = LAST_NAMES[i]
        author = first + " " + last
        year = str(randint(1000, 2024))
        add_function(author, year)


def add_book(author, year):
    book = {
        "author": author,
        "title": "Pythonin alkeet",
        "year": year,
        "publisher": "Otava",
    }
    util.validate_book(book["author"], book["title"], book["year"], book["publisher"])
    references.add_book(book["author"], book["title"], book["year"], book["publisher"])


def add_article(author, year):
    article = {
        "author": author,
        "title": "Ketterän ohjelmistotuotannon tulevaisuus",
        "journal": "ATK-lehti",
        "volume": "4",
        "number": "2",
        "year": year,
        "pages_from": "89",
        "pages_to": "98",
        "doi": "0987ktrddt6",
        "url": "https://sisu.helsinki.fi",
    }
    util.validate_article(article)
    references.add_article(article)


def add_inproceedings(author, year):
    inproceedings = {
        "author": author,
        "title": "Ohjelmointi on hauskaa",
        "year": year,
        "booktitle": "Julle Julkaisija",
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


def add_misc(author, year):
    misc = {
        "author": author,
        "title": "Olioperustainen ohjelmointi",
        "year": year,
        "note": "Laudaturtyö : Helsingin yliopisto, Tietojenkäsittelyopin laitos, 1986.",
    }
    util.validate_misc(misc["author"], misc["title"], misc["year"], misc["note"])
    references.add_misc(misc["author"], misc["title"], misc["year"], misc["note"])


if __name__ == "__main__":
    with app.app_context():
        add_data()
