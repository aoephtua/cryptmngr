# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/cryptutils.py

# Standard library imports
import secrets
import string
import uuid

def generate_uuid4_str():
    # Generates uppercase string with UUID4 and without hyphens
    return str(uuid.uuid4()).replace('-', '').upper()

def generate_pwd(length=32):
    # Generates password with letters and digits of specified length
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
