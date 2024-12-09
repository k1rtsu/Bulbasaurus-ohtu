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
            VALUES (:book)
            RETURNING id;
            """
    )
    book_id = db.session.execute(sql, {"book": "book"}).fetchone()[0]

    information = {
        "author": author,
        "title": title,
        "year": year,
        "publisher": publisher,
    }
    for field, value in information.items():
        sql = text(
            """
                INSERT INTO info (reference_id, field, value)
                VALUES (:reference_id, :field, :value);
                """
        )
        db.session.execute(
            sql, {"reference_id": book_id, "field": field, "value": value}
        )

    db.session.commit()


def add_misc(author: str, title: str, year: str, note: str) -> None:
    """Add misc into the database."""
    sql = text(
        """
            INSERT INTO reference (type)
            VALUES (:misc)
            RETURNING id;
            """
    )

    misc_id = db.session.execute(sql, {"misc": "misc"}).fetchone()[0]

    information = {"author": author, "title": title, "year": year, "note": note}

    for field, value in information.items():
        sql = text(
            """
            INSERT INTO info (reference_id, field, value)
            VALUES (:reference_id, :field, :value);
            """
        )

        db.session.execute(
            sql, {"reference_id": misc_id, "field": field, "value": value}
        )

    db.session.commit()


def add_article(article_data: dict) -> None:
    """Add an article into the database."""
    sql = text(
        """
            INSERT INTO reference (type)
            VALUES (:article)
            RETURNING id;
            """
    )
    article_id = db.session.execute(sql, {"article": "article"}).fetchone()[0]

    for field, value in article_data.items():
        sql = text(
            """
            INSERT INTO info (reference_id, field, value)
            VALUES (:reference_id, :field, :value);
            """
        )
        db.session.execute(
            sql, {"reference_id": article_id, "field": field, "value": value}
        )

    db.session.commit()


def add_inproceedings(author, title, year, booktitle) -> None:
    """Add inproceedings into the database."""
    sql = text(
        """
            INSERT INTO reference (type)
            VALUES (:inproceedings)
            RETURNING id;
            """
    )
    inproceedings_id = db.session.execute(sql, {"inproceedings": "inproceedings"}).fetchone()[0]

    information = {
        "author": author,
        "title": title,
        "year": year,
        "booktitle": booktitle,
    }
    for field, value in information.items():
        sql = text(
            """
                INSERT INTO info (reference_id, field, value)
                VALUES (:reference_id, :field, :value);
                """
        )
        db.session.execute(
            sql, {"reference_id": inproceedings_id, "field": field, "value": value}
        )

    db.session.commit()


def get_all_books() -> list[dict]:
    """
    Returns all books from the database.
    Each item in the return list is like: {
        'reference_id': int,
        'book_info: {
                'author': str,
                'title': str,
                'year': str,
                'publisher': str
        }
    }
    """

    sql = text(
        """
        SELECT 
        json_build_object (
        'reference_id', reference_id,
        'book_info', json_object_agg(
                field,
                value
        )
        ) AS book
        FROM info
        WHERE reference_id IN(
        SELECT id 
        FROM reference 
        WHERE type = 'book'
        )
        GROUP BY reference_id;
        """
    )

    query_result = db.session.execute(sql)
    rows = query_result.fetchall()
    books = [row[0] for row in rows]
    return books


def get_all_articles() -> list[dict]:

    sql = text(
        """
        SELECT 
        json_build_object (
        'reference_id', reference_id,
        'article_info', json_object_agg(
                field,
                value
        )
        ) AS article
        FROM info
        WHERE reference_id IN(
        SELECT id 
        FROM reference 
        WHERE type = 'article'
        )
        GROUP BY reference_id;
        """
    )

    query_result = db.session.execute(sql)
    rows = query_result.fetchall()
    articles = [row[0] for row in rows]
    return articles


def remove_reference(reference_id: int) -> None:
    try:
        sql = text(
            """
            DELETE FROM info
            WHERE reference_id = :reference_id;
            """
        )
        db.session.execute(sql, {"reference_id": reference_id})

        sql = text(
            """
            DELETE FROM reference
            WHERE id = :reference_id;
            """
        )
        db.session.execute(sql, {"reference_id": reference_id})

        db.session.commit()

    except Exception as e:
        db.session.rollback()
        raise RuntimeError(
            f"Failed to remove reference with ID {reference_id}: {e}"
        ) from e


def get_all_misc() -> list[dict]:

    sql = text(
        """
        SELECT 
        json_build_object (
        'reference_id', reference_id,
        'misc_info', json_object_agg(
                field,
                value
        )
        ) AS misc
        FROM info
        WHERE reference_id IN (
            SELECT id 
            FROM reference 
            WHERE type = 'misc'
        )
        GROUP BY reference_id;
        """
    )

    query_result = db.session.execute(sql)
    rows = query_result.fetchall()
    misc_references = [row[0] for row in rows]
    return misc_references


def get_all_inproceedings() -> list[dict]:
    """
    Returns all inproceedings from the database.
    Each item in the return list is like: {
        'reference_id': int,
        'inproceedings_info: {
                'author': str,
                'title': str,
                'year': str,
                'booktitle': str
        }
    }
    """
    sql = text(
        """
        SELECT 
        json_build_object (
        'reference_id', reference_id,
        'inproceedings_info', json_object_agg(
                field,
                value
        )
        ) AS inproceedings
        FROM info
        WHERE reference_id IN(
        SELECT id 
        FROM reference 
        WHERE type = 'inproceedings'
        )
        GROUP BY reference_id;
        """
    )

    query_result = db.session.execute(sql)
    rows = query_result.fetchall()
    inproceedings = [row[0] for row in rows]
    return inproceedings
