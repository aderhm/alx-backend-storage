#!/usr/bin/env python3
"""Module: Inserts a new document
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
