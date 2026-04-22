#!/usr/bin/env python3

"""11-schools_by_topic.py
"""


def schools_by_topic(mongo_collection, topic: str):
    """Get schools by topics

    Args:
        mongo_collection: Mongo collection
        topic (str): Topic to find schools

    Return:
        Schools that contains topic
    """
    schools = []

    for school in mongo_collection.find():
        topics = school.get('topics')

        if topics:
            if topic in topics:
                schools.append(school)

    return schools
