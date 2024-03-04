# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/datetimeutils.py

# Standard library imports
from datetime import datetime, timezone

def get_utc_now():
    # Gets current datetime with UTC timezone
    utc = timezone.utc
    return datetime.now(utc)
