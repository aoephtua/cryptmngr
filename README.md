# cryptmngr

Python based CLI tool to manage and store directories (CRUD) and process encryption and decryption.

## Usage

    $ cryptmngr [OPTIONS] COMMAND [ARGS]...

### General Options

```
Options:
--help  Show this message and exit.
```

### Commands

- [create-dir](#create-dir)
- [decrypt](#decrypt-encrypt)
- [delete-dir](#delete-dir)
- [encrypt](#decrypt-encrypt)                         
- [list-dir](#list-dir)
- list-dirs

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

#### decrypt encrypt

```
Arguments:
  alias [ALIAS]  TEXT  [default: os.getcwd().split(os.sep)[-1]]
Options:
--force-all            [default: no-force-all]
```

#### delete-dir

```
Arguments:
  alias [ALIAS]  TEXT  [default: None]
```

#### list-dir

```
Arguments:
  alias [ALIAS]  TEXT  [default: os.getcwd().split(os.sep)[-1]]
```

## Requirements

- [cryptdir](https://github.com/aoephtua/cryptdir)
- [MongoDB](https://github.com/mongodb/mongo)

See [requirements.txt](https://github.com/aoephtua/cryptmngr/blob/main/requirements.txt) to install PyPI dependencies.

## License

This project is licensed under [MIT](https://github.com/aoephtua/cryptmngr/blob/main/LICENSE).