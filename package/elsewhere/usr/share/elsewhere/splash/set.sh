#!/usr/bin/env bash

DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
/usr/bin/fim --quiet "$DIRECTORY/images/splash.png" --execute-script "$DIRECTORY/script.txt"
