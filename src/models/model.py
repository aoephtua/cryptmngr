# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/models/model.py

# Local imports
from datetimeutils import get_utc_now
from mongodb import (
    get_collection as get_db_collection,
    get_document as get_db_document
)

class Model():
    # Base class to inherit from
    @staticmethod
    def get_collection(collection_name):
        # Gets database collection by name
        return get_db_collection('cryptmngr', collection_name)
    
    @classmethod
    def get_filter_dict(cls, filter):
        # Gets filter value as dict
        return (
            filter if type(filter) is dict
            else { cls.primary_key: filter }
        )

    @classmethod
    def get_document(cls, filter):
        # Gets instance of document by filter
        return cls.documents.find_one(
            cls.get_filter_dict(filter)
        )

    @classmethod
    def get_documents(cls, filter = None, sort = None):
        # Gets sorted instances of codes by specified filter
        documents = cls.documents.find(filter).sort(sort or cls.primary_key)
        return list(documents)

    @classmethod
    def create_document(cls, args):
        # Creates document by arguments
        db_doc = get_db_document(cls.schema, args)
        filter = (
            cls.get_creation_filter(db_doc) if hasattr(cls, 'get_creation_filter')
            else { cls.primary_key: db_doc.get(cls.primary_key) }
        )
        document = cls.get_document(filter)
        if not document:
            if cls.before_insert:
                cls.before_insert(db_doc, args)
            document = {
                **db_doc,
                'created_at': get_utc_now()
            }
            return cls.documents.insert_one(document)
    
    @staticmethod
    def get_value_by_type(value, type):
        # Gets value by type
        match type.__name__:
            case 'bool':
                return value.lower() == 'true'
        return value

    @classmethod
    def update_document(cls, filter, key, value):
        # Updates document by arguments
        if key in cls.schema and value is not None:
            document = {}
            document[key] = Model.get_value_by_type(
                value,
                cls.schema[key]
            )
            document['updated_at'] = get_utc_now()
            return cls.documents.update_one(
                cls.get_filter_dict(filter),
                { '$set': document }
            )

    @classmethod
    def delete_document(cls, filter):
        # Deletes document by specified filter
        return cls.documents.delete_one(
            cls.get_filter_dict(filter)
        )
