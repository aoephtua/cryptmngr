$basedir = Split-Path $MyInvocation.MyCommand.Definition

& "python" "$basedir/src/main.py" $args
