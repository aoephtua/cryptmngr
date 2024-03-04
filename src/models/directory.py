# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/models/directory.py

# Standard library imports
import os

# Local imports
from cryptutils import generate_uuid4_str, generate_pwd
from models.model import Model

class Directory(Model):
    # String with name of database collection
    collection_name = 'directories'

    # MongoDB collection of directories
    documents = Model.get_collection(collection_name)

    # String with primary key of directory
    primary_key = 'alias'
    
    # Dictionary with schema of directory
    schema = {
        'alias': str,
        'src_dir': str,
        'enc_dir': str,
        'filter': str,
        'pwd': str
    }

    def get_creation_filter(db_doc):
        # Gets dictionary with creation filter
        return {
            'alias': db_doc.get('alias'),
            'src_dir': db_doc.get('src_dir')
        }
    
    def before_insert(doc, args):
        # Sets directory values before insert
        enc_dir = doc.get('enc_dir')
        if enc_dir:
            if args.get('force_enc_id'):
                enc_id = generate_uuid4_str()
                enc_dir = os.path.join(enc_dir, enc_id)
                doc.update({ 'enc_dir': enc_dir })
        if not doc.get('pwd'):
            doc.update({ 'pwd': generate_pwd(48) })
