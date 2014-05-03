#!/bin/bash

NAME="$1"
FROM="$2"

if [[ -z "$NAME" ]]
then
    echo "No name given."
    exit 1
fi

if [[ -z "$FROM" ]]
then
    FROM="myapp"
fi

sed -i -e "s/$FROM/$NAME/g" runserver.py mysql_init.sql config_defaults.py alembic/env.py
mv "$FROM" "$NAME"

