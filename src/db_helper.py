from config import db, app
from sqlalchemy import text


# KOPIOITU ESIMERKISTÄ JA LUOTU ESIMERKIN MUKAAN TESTI -NIMINEN TAULU, TIETOKANNAN TOIMIVUUDEN TESTAAMISEKSI.
# SETUP_DB() VOISI LUODA KAIKKI MEIDÄN TARVITSEMAT TAULUT JA RESET_DB RESETOIDA NE KAIKKI

# table_name = "testi"
tables = ["reference", "author", "book"]


def reset_db():
    """Delete the contents of all tables"""
    for table in tables:
        print(f"Clearing contents from table {table}")
        sql = text(f"DELETE FROM {table}")
        db.session.execute(sql)
        db.session.commit()


def setup_db():
    """Deletes tables and creates them again"""

    for table in tables:
        print(f"Checking if table {table} exists")
        if table_exists(table):
            print(f"Table {table} exists, dropping")
            delete_table(table)

    print("Creating table reference")
    sql = text(
        """
        CREATE TABLE reference
        (
            id SERIAL PRIMARY KEY,
            type TEXT
        );"""
    )
    db.session.execute(sql)
    db.session.commit()

    print("Creating table author")
    sql = text(
        """
        CREATE TABLE author
        (
            id SERIAL PRIMARY KEY,
            reference_id INTEGER REFERENCES reference,
            name TEXT
        );"""
    )
    db.session.execute(sql)
    db.session.commit()

    print("Creating table book")
    sql = text(
        """
        CREATE TABLE book
        (
            id SERIAL PRIMARY KEY,
            reference_id INTEGER REFERENCES reference,
            title TEXT,
            year INTEGER,
            publisher TEXT
        );"""
    )
    db.session.execute(sql)
    db.session.commit()


def table_exists(table):
    """Check if table exists"""
    sql_table_existence = text(
        "SELECT EXISTS ("
        "  SELECT 1"
        "  FROM information_schema.tables"
        f" WHERE table_name = '{table}'"
        ")"
    )
    # print(sql_table_existence)

    result = db.session.execute(sql_table_existence)
    return result.fetchall()[0][0]


def delete_table(table):
    """Delete table"""
    sql = text(f"DROP TABLE {table} CASCADE")
    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
