# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/cli.py

def print_dict(dict):
    # Prints formatted dictionary
    for key in dict:
        print(f'{key}: {dict[key]}')

def list_docs(model):
    # Lists documents
    docs = model.get_documents()
    for idx, doc in enumerate(docs):
        if idx > 0:
            print()
        print_dict(doc)

def list_doc(model, filter):
    # Lists one document by filter
    doc = model.get_document(filter)
    if doc:
        print_dict(doc)

def create_doc(model, key, args):
    # Creates document by arguments
    result = model.create_document(args)
    if result:
        inserted_id = result.inserted_id
        doc = model.get_document({ '_id': inserted_id })
        print_dict(doc)
    else:
        model_name = model.__name__
        print(f'Error: {model_name} "{key}" already exists')

def update_doc(model, filter, key, value):
    # Updates document by arguments
    res = model.update_document(filter, key, value)
    if res:
        print(f'Updated count: {res.modified_count}')
        list_doc(model, filter)
    else:
        print('Error: Invalid arguments')

def delete_doc(model, key):
    # Deletes document by key
    res = model.delete_document(key)
    print(f'Deleted count: {res.deleted_count}')
