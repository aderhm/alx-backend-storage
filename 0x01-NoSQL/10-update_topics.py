#!/usr/bin/env python3
"""Module: Changes all topics of a school document
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name
    """
    filter = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter, update)
