"""
MongoDB list documents in collection
"""


def list_all(mongo_collection):
    """List all documents

    Args:
        mongo_collection: Mongo collection to list

    Returns:
        list: List of documents
    """

    return mongo_collection.find()
