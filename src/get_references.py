"""Functions to get data from the database.

Functions:

    get_reference_info_by_id
"""

from sqlalchemy import text
from config import db


def get_reference_info_by_id(reference_id: int | str) -> tuple[dict, str]:
    """
    Return all info of a reference.

    Arguments:

        reference_id: id of the reference we want to return"""
    reference_id = int(reference_id)
    sql = text(
        """
        SELECT id, type
        FROM reference
        WHERE id=:reference_id
        """
    )
    reference = db.session.execute(sql, {"reference_id": reference_id})
    reference = reference.fetchone()
    info = {"id": reference[0], "type": reference[1]}

    sql = text(
        """
        SELECT id, reference_id, field, value
        FROM info
        WHERE reference_id=:reference_id
        """
    )
    reference_info = db.session.execute(sql, {"reference_id": reference_id})
    reference_info = reference_info.fetchall()

    for row in reference_info:
        info[row[2]] = {"info_id": row[0], "field": row[3]}

    return info


def reference_exists(reference_id: int | str) -> bool:
    """Check whether a reference by the given id exists."""
    reference_id = int(reference_id)

    sql = text(
        """
        SELECT id
        FROM reference
        WHERE id=:reference_id
        """
    )
    exists = db.session.execute(sql, {"reference_id": reference_id})
    exists = exists.fetchone()

    print()
    print("exists is", exists)
    print()
    if exists is None:
        exists = False
    else:
        exists = True

    return exists
