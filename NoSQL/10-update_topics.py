#!/usr/bin/env python3

"""10-update_topics.py
"""


def update_topics(mongo_collection, name: str, topics: list):
    """Update topics

    Args:
        mongo_collection:
        name (str): Name
        topics (list): List of topics
    """

    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
