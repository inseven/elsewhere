#!/usr/bin/env bash

set -e
set -o pipefail
set -u

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="$SCRIPTS_DIRECTORY/.."
SOURCE_DIRECTORY="$ROOT_DIRECTORY/package"

font="fonts/Inter/static/Inter-Thin.ttf"

echo "Generating splash screens..."
SPLASH_BUILD_DIRECTORY="$SOURCE_DIRECTORY/elsewhere/usr/share/elsewhere/splash/images"
if [ -d "$SPLASH_BUILD_DIRECTORY" ] ; then
    rm -r "$SPLASH_BUILD_DIRECTORY"
fi
mkdir -p "$SPLASH_BUILD_DIRECTORY"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" -size 100x100 -pointsize 24 label:"1.0.0" -geometry +0+240 -composite "$SPLASH_BUILD_DIRECTORY/splash.png"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 32 -gravity center label:"Shutting Down..." "$SPLASH_BUILD_DIRECTORY/shutting-down.png"

echo "Generating local Python cache..."
export PYTHONUSERBASE="$SOURCE_DIRECTORY/elsewhere/usr/share/elsewhere/python"
if [ -d "$PYTHONUSERBASE" ] ; then
    rm -r "$PYTHONUSERBASE"
fi
mkdir -p "$PYTHONUSERBASE"
export PATH="$PYTHONUSERBASE/bin":$PATH
pip3 install --user -r "$SOURCE_DIRECTORY/requirements.txt"

echo "Building Debian package..."
cd package
dpkg-deb --build elsewhere