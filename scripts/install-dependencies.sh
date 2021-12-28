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

# Install the Python dependencies
pip3 install --user pipenv
PIPENV_PIPFILE="$CHANGES_DIRECTORY/Pipfile" pipenv install --verbose

# Install the GitHub CLI
github_cli_url="https://github.com"`curl -s -L https://github.com/cli/cli/releases/latest | grep -o -e "/.*armv6.*tar.gz"`
if [ -d "$GITHUB_CLI_PATH" ] ; then
    rm -r "$GITHUB_CLI_PATH"
fi
mkdir -p "$GITHUB_CLI_PATH"
curl --location "$github_cli_url" --output "cli.tar.gz"
tar --strip-components 1 -zxv -f "cli.tar.gz" -C "$GITHUB_CLI_PATH"
unlink "cli.tar.gz"
