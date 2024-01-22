# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/main.py

# Standard library imports
import os

# Third party imports
import typer
from typing_extensions import Annotated

# Local imports
from cryptmngr import (
    encrypt as encrypt_dir,
    decrypt as decrypt_dir
)
from directory import (
    get_directory,
    get_directories,
    create_directory,
    delete_directory
)

# Instance of Typer
app = typer.Typer()

# Current working directory
working_dir = os.getcwd()

# Current folder name of working directory
dir_name = working_dir.split(os.sep)[-1]

@app.command()
def encrypt(
    alias: Annotated[str, typer.Argument()] = dir_name,
    force_all: bool = False):
    # Encrypts directories
    encrypt_dir(alias, force_all)

@app.command()
def decrypt(
    alias: Annotated[str, typer.Argument()] = dir_name,
    force_all: bool = False):
    # Decrypts directories
    decrypt_dir(alias, force_all)

@app.command()
def list_dir(alias: Annotated[str, typer.Argument()] = dir_name):
    # Lists directory by alias
    dir = get_directory({ 'alias': alias })
    print(dir)

@app.command()
def list_dirs():
    # Lists all directories
    dirs = get_directories()
    for dir in dirs:
        print(dir)

@app.command()
def create_dir(
        alias: Annotated[str, typer.Option()] = dir_name,
        src_dir: Annotated[str, typer.Option()] = working_dir,
        enc_dir: str = None,
        filter: str = None,
        pwd: str = None,
        force_enc_id: bool = False):
    # Creates directory by arguments
    result = create_directory({
        'alias': alias,
        'src_dir': src_dir,
        'enc_dir': enc_dir,
        'filter': filter,
        'pwd': pwd
    }, force_enc_id)
    if result:
        inserted_id = result.inserted_id
        dir = get_directory({ '_id': inserted_id })
        print(dir)
    else:
        print(f'Error: Directory "{src_dir}" already exists')

@app.command()
def delete_dir(alias: Annotated[str, typer.Argument()]):
    # Deletes directory by alias
    res = delete_directory(alias)
    print(f'Deleted count: {res.deleted_count}')

# Only runs when file is executed as a script
if __name__ == '__main__':
    app()
