#!/usr/bin/env bash

set -e
set -o pipefail
set -u

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="$SCRIPTS_DIRECTORY"
SOURCE_DIRECTORY="$ROOT_DIRECTORY/package"

font="fonts/Inter/static/Inter-Thin.ttf"

SPLASH_BUILD_DIRECTORY=package/elsewhere/usr/share/elsewhere/splash/images

echo "Generating splash screens..."
mkdir -p "$SPLASH_BUILD_DIRECTORY"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" "$SPLASH_BUILD_DIRECTORY/splash.png"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 32 -gravity center label:"Shutting Down..." "$SPLASH_BUILD_DIRECTORY/shutting-down.png"

echo "Generating local Python cache..."
export PYTHONUSERBASE="$ROOT_DIRECTORY/package/elsewhere/usr/share/elsewhere/python"
if [ -d "$PYTHONUSERBASE" ] ; then
    rm -r "$PYTHONUSERBASE"
fi
mkdir -p "$PYTHONUSERBASE"
export PATH="$PYTHONUSERBASE/bin":$PATH
pip3 install --user -r "$SOURCE_DIRECTORY/requirements.txt"

echo "Building Debian package..."
cd package
dpkg-deb --build elsewhere
