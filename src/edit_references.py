"""
Functions to edit references in the database.
"""

from sqlalchemy import text
from config import db


def update_reference(form_data: dict, reference_id: str):
    """Update the information of a reference.

    Arguments:
        form_data: a dictionary that has the updated information.
    """
    reference_id = int(reference_id)

    for key, value in form_data.items():
        sql = text(
            """
            UPDATE info
            SET value = :value
            WHERE field=:field AND reference_id=:reference_id;
            """
        )
        db.session.execute(
            sql, {"value": value, "field": key, "reference_id": reference_id}
        )
    db.session.commit()
