# cryptmngr

Python based CLI tool to manage and store directories (CRUD) and process encryption and decryption.

## Usage

    $ cryptmngr [OPTIONS] COMMAND [ARGS]...

### General Options

```
Options:
--help  Show this message and exit.
```

### Command Summary

#### Codes

* [list-codes](#list-codes)
* [list-code](#list-code)
* [create-code](#create-code)
* [update-code](#update-code)
* [delete-code](#delete-code)

#### Directories

* [list-dirs](#list-dirs)
* [list-dir](#list-dir)
* [create-dir](#create-dir)
* [update-dir](#update-dir)
* [delete-dir](#delete-dir)


#### Processing

* [encrypt](#encrypt-decrypt)
* [decrypt](#encrypt-decrypt)

### Command Details

##### list-codes

No options and arguments available.

#### list-code

```
Arguments:
* name [NAME]  TEXT  [default: None] [required]
```

#### create-code

```
Arguments:
* file_path [FILE_PATH]  TEXT  [default: None] [required]
Options:
--name                   TEXT  [default: os.path.basename(file_path)]
--cmd                    TEXT  [default: encrypt]
--exec                   TEXT  [default: post]
--all                          [default: all]
--disabled                     [default: no-disabled]
```

#### update-code

```
Arguments:
* name [NAME]  TEXT  [default: None] [required]
Options:
* --key        TEXT  [default: None] [required]
* --value      TEXT  [default: None] [required]
```

#### delete-code

```
Arguments:
* name [NAME]  TEXT  [default: None] [required]
```

#### list-dirs

No options and arguments available.

#### list-dir

```
Arguments:
  alias [ALIAS]  TEXT  [default: os.getcwd().split(os.sep)[-1]]
```

#### create-dir

```
Options:
--alias         TEXT  [default: os.getcwd().split(os.sep)[-1]]
--src-dir       TEXT  [default: os.getcwd()]
--enc-dir       TEXT  [default: None]
--filter        TEXT  [default: None]
--pwd           TEXT  [default: None]
--force-enc-id        [default: no-force-enc-id]
```

#### update-dir

```
Arguments:
* alias [ALIAS]  TEXT  [default: None] [required]
Options:
* --key          TEXT  [default: None] [required]
* --value        TEXT  [default: None] [required]
```

#### delete-dir

```
Arguments:
* alias [ALIAS]  TEXT  [default: None] [required]
```

#### encrypt decrypt

```
Arguments:
  alias [ALIAS]  TEXT  [default: os.getcwd().split(os.sep)[-1]]
Options:
--force-all            [default: no-force-all]
```

## Requirements

- [cryptdir](https://github.com/aoephtua/cryptdir)
- [MongoDB](https://github.com/mongodb/mongo)

See [requirements.txt](https://github.com/aoephtua/cryptmngr/blob/main/requirements.txt) to install PyPI dependencies.

## License

This project is licensed under [MIT](https://github.com/aoephtua/cryptmngr/blob/main/LICENSE).