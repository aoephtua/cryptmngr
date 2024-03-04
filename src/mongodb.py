# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/mongodb.py

# Third party imports
from pymongo import MongoClient

# Global instance of MongoClient
mongo_client = None

def get_mongodb_client(uri = 'mongodb://localhost:27017'):
    # Gets instance of MongoClient
    global mongo_client
    if not mongo_client:
        mongo_client = MongoClient(uri)
    return mongo_client

def get_database(name):
    # Get database by name
    client = get_mongodb_client()
    return client[name]

def get_collection(db_name, name):
    # Get database collection by name
    db = get_database(db_name)
    return db[name]

def get_document(schema, args):
    # Gets document with arguments by keys and values
    doc = {}
    for key in schema:
        value = args.get(key)
        if value is not None:
            doc[key] = value
    return doc
