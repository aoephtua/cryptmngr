# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/models/code.py

# Local imports
from models.model import Model

class Code(Model):
    # String with name of database collection
    collection_name = 'codes'

    # MongoDB collection of codes
    documents = Model.get_collection(collection_name)

    # String with primary key of code
    primary_key = 'name'

    # Dictionary with schema of code
    schema = {
        'name': str,
        'cmd': str,
        'exec': str,
        'all': bool,
        'enabled': bool
    }

    def before_insert(doc, args):
        # Sets code values before insert
        file_path = args.get('file_path')
        with open(file_path) as file:
            code_str = file.read()
            doc.update({ 'code_str': code_str })
