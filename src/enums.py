# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/enums.py

# Standard library imports
from enum import Enum

class Cmd(str, Enum):
    # Class with collection of keys values for Cmd
    encrypt = 'encrypt',
    decrypt = 'decrypt'

class Exec(str, Enum):
    # Class with collection of keys values for Exec
    pre = 'pre',
    post = 'post'
