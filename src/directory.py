# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/directory.py

# Standard library imports
import os
from datetime import datetime, timezone

# Third party imports
from mongodb import get_collection, get_document

# Local imports
from cryptutils import generate_uuid4_str, generate_pwd

# MongoDB collection of dictionaries
directories = get_collection('cryptmngr', 'directories')

# Array with entries of directory
entries = [
    'alias',
    'src_dir',
    'enc_dir',
    'filter',
    'pwd'
]

def get_utc_now():
    # Gets current datetime with UTC timezone
    utc = timezone.utc
    return datetime.now(utc)

def get_directory(filter):
    # Gets instance of directory by specified filter
    return directories.find_one(filter)

def get_directories(filter = None, sort = 'alias'):
    # Gets sorted instances of directories by specified filter
    return directories.find(filter).sort(sort)

def create_directory(args, force_enc_id):
    # Creates directory by arguments
    directory = get_document(entries, args)
    filter = {
        'alias': directory.get('alias'),
        'src_dir': directory.get('src_dir')
    }
    dir = get_directory(filter)
    if not dir:
        enc_dir = directory.get('enc_dir')
        if enc_dir:
            if force_enc_id:
                enc_id = generate_uuid4_str()
                enc_dir = os.path.join(enc_dir, enc_id)
                directory.update({ 'enc_dir': enc_dir })
        if not directory.get('pwd'):
            directory.update({ 'pwd': generate_pwd(48) })
        dir = {
            **directory,
            'created_at': get_utc_now()
        }
        return directories.insert_one(dir)

def update_directory(alias, key, value):
    # Updates directory by arguments
    if key in entries and value is not None:
        dir = {}
        dir[key] = value
        dir['updated_at'] = get_utc_now()
        return directories.update_one(
            { 'alias': alias },
            { '$set': dir }
        )
    
def delete_directory(alias):
    # Deletes directory by specified alias
    return directories.delete_one({ 'alias': alias })
