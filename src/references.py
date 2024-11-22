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

def add_article(article_data: dict) -> None:
    """Add an article into the database."""
    sql = text(
            """
            INSERT INTO reference (type)
            VALUES (:article);
            """
    )
    db.session.execute(sql, {"article": "article"})

    sql = text(
            """
            SELECT id
            FROM reference
            ORDER BY id DESC
            LIMIT 1;
            """
            )
    article_id = db.session.execute(sql)
    article_id = article_id.fetchone()[0]

    for field, value in article_data.items():
        sql = text(
            """
            INSERT INTO info (reference_id, field, value)
            VALUES (:reference_id, :field, :value);
            """
        )
        db.session.execute(sql, {"reference_id": article_id, "field": field, "value": value})

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
