#!/bin/bash

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="${SCRIPTS_DIRECTORY}/.."
export CHANGES_DIRECTORY="${SCRIPTS_DIRECTORY}/changes"

export PATH="${CHANGES_DIRECTORY}":$PATH

export PYTHONUSERBASE="${ROOT_DIRECTORY}/.local/python"
mkdir -p "$PYTHONUSERBASE"
export PATH="${PYTHONUSERBASE}/bin":$PATH

export GITHUB_CLI_PATH="${ROOT_DIRECTORY}/.local/gh"
mkdir -p "$GITHUB_CLI_PATH"
export PATH="${GITHUB_CLI_PATH}/bin":$PATH
