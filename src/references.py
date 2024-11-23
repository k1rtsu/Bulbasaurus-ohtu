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


def add_misc(author: str, title: str, year: str, month: str, note: str) -> None:
    """Add misc into the database."""
    sql = text(
            """
            INSERT INTO reference (type)
            VALUES (:misc);
            """
    )

    db.session.execute(sql, {"type":"misc"})

    sql = text(
        """
        SELECT id 
        FROM reference
        ORDER BY id DESC
        LIMIT 1;
        """)

    misc_id = db.session.execute(sql).fetchone()[0]

    information = {"author": author, "title": title, "year": year, "month": month, "note": note}

    for field, value in information.items():
        sql = text(
            """
            INSERT INTO info (reference_id, field, value)
            VALUES (:reference_id, :field, :value);
            """
        )

        db.session.execute(sql, {"reference_id": misc_id, "field": field, "value": value})

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
        raise RuntimeError(f"Failed to remove reference with ID {reference_id}: {e}") from e

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
