# Copyright (c) 2024, Thorsten A. Weintz. All rights reserved.
# Licensed under the MIT license. See LICENSE in the project root for license information.

# src/main.py

# Standard library imports
import os

# Third party imports
import typer
from typing_extensions import Annotated

# Local imports
from cli import (
    list_docs,
    list_doc,
    create_doc,
    update_doc,
    delete_doc
)
from cryptmngr import (
    encrypt as encrypt_dir,
    decrypt as decrypt_dir
)
from enums import Cmd, Exec
from models.code import Code
from models.directory import Directory

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
def list_code(
    name: Annotated[str, typer.Argument()]):
    # Lists code by name
    list_doc(Code, name)

@app.command()
def list_codes():
    # Lists all codes
    list_docs(Code)

@app.command()
def create_code(
    file_path: Annotated[str, typer.Argument()],
    name: Annotated[str, typer.Option()] = '',
    cmd: Annotated[Cmd, typer.Option()] = Cmd.encrypt,
    exec: Annotated[Exec, typer.Option()] = Exec.post,
    all: Annotated[bool, typer.Option()] = True,
    disabled: bool = False):
    # Creates code by arguments
    file_path = os.path.abspath(file_path)
    if os.path.exists(file_path):
        if not name:
            name = os.path.basename(file_path)
        enabled = not disabled
        create_doc(Code, name, locals())
    else:
        print(f'File "{file_path}" not found')

@app.command()
def update_code(
    name: Annotated[str, typer.Argument()],
    key: Annotated[str, typer.Option()],
    value: Annotated[str, typer.Option()]):
    # Updates code by arguments
    update_doc(Code, name, key, value)

@app.command()
def delete_code(name: Annotated[str, typer.Argument()]):
    # Deletes code by name
    delete_doc(Code, name)

@app.command()
def list_dir(
    alias: Annotated[str, typer.Argument()] = dir_name):
    # Lists directory by alias
    list_doc(Directory, alias)

@app.command()
def list_dirs():
    # Lists all directories
    list_docs(Directory)

@app.command()
def create_dir(
    alias: Annotated[str, typer.Option()] = dir_name,
    src_dir: Annotated[str, typer.Option()] = working_dir,
    enc_dir: str = None,
    filter: str = None,
    pwd: str = None,
    force_enc_id: bool = False):
    # Creates directory by arguments
    create_doc(Directory, src_dir, locals())

@app.command()
def update_dir(
    alias: Annotated[str, typer.Argument()],
    key: Annotated[str, typer.Option()],
    value: Annotated[str, typer.Option()]):
    # Updates directory by arguments
    update_doc(Directory, alias, key, value)

@app.command()
def delete_dir(alias: Annotated[str, typer.Argument()]):
    # Deletes directory by alias
    delete_doc(Directory, alias)

# Only runs when file is executed as a script
if __name__ == '__main__':
    app()
