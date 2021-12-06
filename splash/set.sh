#!/usr/bin/env bash

DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
fim --quiet "$DIRECTORY/splash.png" --execute-script "$DIRECTORY/script.txt"
