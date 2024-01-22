# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/cryptmngr.py

# Standard library imports
import os

# Third party imports
from colorama import Fore, Style

# Local imports
from directory import (
    get_directory,
    get_directories
)
    
def get_opts_with_args(dir, entries):
    # Gets string with options and arguments
    opts = ''
    for key, opt in entries.items():
        value = dir.get(key)
        if value:
            if opts != '':
                opts += ' '
            opts += f'--{opt} "{value}"'
    return opts

def get_directories_for_cmd(alias = None, force_all = False):
    # Gets array with directories for command process
    if alias:
        dir = get_directory({ 'alias': alias })
        if dir:
            return [dir]
    elif force_all:
        return get_directories()

def proc_cryptdir_cmd(cmd, alias = None, force_all = False):
    # Processes cryptdir command
    dirs = get_directories_for_cmd(alias, force_all)
    entries = {
        'pwd': 'password',
        'src_dir': 'src-directory',
        'enc_dir': 'enc-directory'
    }
    if cmd == 'encrypt':
        entries['filter'] = 'filter'
    if dirs:
        for dir in dirs:
            opts = get_opts_with_args(dir, entries)
            command = f'cryptdir {cmd}{f' {opts}' if opts != '' else ''}'
            print(Fore.CYAN + command + Style.RESET_ALL)
            os.system(command)
    else:
        print('No directories found')

def encrypt(alias = None, force_all = False):
    # Encrypts directories
    proc_cryptdir_cmd('encrypt', alias, force_all)

def decrypt(alias = None, force_all = False):
    # Decrypts directories
    proc_cryptdir_cmd('decrypt', alias, force_all)
