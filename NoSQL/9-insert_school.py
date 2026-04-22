#!/usr/bin/env python3

"""
9-insert_school.py
"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document in a collection

    Args:
        mongo_collection: Collection to insert document in

    Returns:
        _id of the new document
    """

    return mongo_collection.insert_one(kwargs).inserted_id
