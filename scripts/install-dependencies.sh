#!/bin/bash

set -e
set -o pipefail
set -x
set -u

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="${SCRIPTS_DIRECTORY}/.."
CHANGES_DIRECTORY="${SCRIPTS_DIRECTORY}/changes"

ENVIRONMENT_PATH="${SCRIPTS_DIRECTORY}/environment.sh"

source "$ENVIRONMENT_PATH"

# Remove the existing Python user directory.
if [ -d "$PYTHONUSERBASE" ] ; then
    rm -r "$PYTHONUSERBASE"
fi
mkdir -p "$PYTHONUSERBASE"

# Install the Python dependencies
pip3 install --user pipenv
PIPENV_PIPFILE="$CHANGES_DIRECTORY/Pipfile" pipenv install --verbose
