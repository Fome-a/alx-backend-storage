#!/usr/bin/env python3
"""Return a list of documents within a collection"""


def list_all(mongo_collection):
    """returns a list of documents"""
    return list(mongo_collection.find())
