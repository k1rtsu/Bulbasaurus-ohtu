"""Functions to get data from the database.

Functions:

    get_reference_info_by_id
"""

from sqlalchemy import text
from config import db


def get_reference_info_by_id(reference_id: int) -> tuple[dict, str]:
    """
    Return all info of a reference.
    
    Arguments:
<<<<<<< HEAD
        reference_id: id of the reference we want to return"""
=======
        reference_id: id of the reference"""
>>>>>>> 5410b82 (Add form for editing references)
    reference_id = int(reference_id)
    sql = text(
        """
        SELECT type
        FROM reference
        WHERE id=:reference_id
        """
    )
    reference_type = db.session.execute(sql, {"reference_id": reference_id})
    reference_type = reference_type.fetchone()
<<<<<<< HEAD
=======
    print()
    print(reference_type)
>>>>>>> 5410b82 (Add form for editing references)
    reference_type = reference_type[0]

    sql = text(
        """
        SELECT id, reference_id, field, value
        FROM info
        WHERE reference_id=:reference_id
        """
    )
    reference_info = db.session.execute(sql, {"reference_id": reference_id})
    reference_info = reference_info.fetchall()

    info = {}
    for row in reference_info:
        info[row[2]] = {"info_id": row[0], "field": row[3]}

    return info, reference_type
