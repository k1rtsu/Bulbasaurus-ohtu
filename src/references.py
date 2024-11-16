"""
Functions to add and fetch data from the database.

Functions:

        add_book(author: str, title: str, year: str, publisher: str) -> None:
"""
from sqlalchemy import text
from config import db

def add_book(author: str, title: str, year: str, publisher: str) -> None:
    """Add a book into the database."""
    sql = text(
            """
            INSERT INTO reference (type)
            VALUES (:book);
            """
    )
    db.session.execute(sql, {"book": "book"})

    sql = text(
            """
            SELECT id
            FROM reference
            ORDER BY id DESC
            LIMIT 1;
            """
            )
    book_id = db.session.execute(sql)
    book_id = book_id.fetchone()[0]

    information = {"author": author, "title": title, "year": year, "publisher": publisher}
    for field, value in information.items():
        sql = text(
                """
                INSERT INTO info (reference_id, field, value)
                VALUES (:reference_id, :field, :value);
                """
        )
        db.session.execute(sql, {"reference_id": book_id, "field": field, "value": value})

    db.session.commit()
