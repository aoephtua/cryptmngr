# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/mongodb.py

# Third party imports
from pymongo import MongoClient

def get_mongodb_client(uri='mongodb://localhost:27017'):
    # Gets instance of MongoClient
    return MongoClient(uri)

def get_database(name):
    # Get database by name
    client = get_mongodb_client()
    return client[name]

def get_collection(db_name, name):
    # Get database collection by name
    db = get_database(db_name)
    return db[name]

def get_document(entries, args):
    # Gets document with arguments by keys and values
    dir = {}
    for x in range(0, len(entries)):
        value = args[x]
        if value is not None:
            dir[entries[x]] = value
    return dir
