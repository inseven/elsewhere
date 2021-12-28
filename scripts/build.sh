#!/usr/bin/env bash

set -e
set -o pipefail
set -u

SCRIPTS_DIRECTORY="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIRECTORY="$SCRIPTS_DIRECTORY/.."
SOURCE_DIRECTORY="$ROOT_DIRECTORY/package"
BUILD_DIRECTORY="$ROOT_DIRECTORY/build"

font="fonts/Inter/static/Inter-Thin.ttf"

source "${SCRIPTS_DIRECTORY}/environment.sh"

INSTALL=${INSTALL:-false}
while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -i|--install)
        INSTALL=true
        shift
        ;;
        *)
        POSITIONAL+=("$1")
        shift
        ;;
    esac
done

echo "Cleaning build directory..."
if [ -d "$BUILD_DIRECTORY" ] ; then
    rm -r "$BUILD_DIRECTORY"
fi
mkdir -p "$BUILD_DIRECTORY"

echo "Getting current version..."
VERSION=$( changes version )

echo "Generating splash screens..."
SPLASH_BUILD_DIRECTORY="$SOURCE_DIRECTORY/elsewhere/usr/share/elsewhere/splash/images"
if [ -d "$SPLASH_BUILD_DIRECTORY" ] ; then
    rm -r "$SPLASH_BUILD_DIRECTORY"
fi
mkdir -p "$SPLASH_BUILD_DIRECTORY"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" -size 100x100 -pointsize 24 label:"${VERSION}" -geometry +0+240 -composite "$SPLASH_BUILD_DIRECTORY/splash.png"
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
PACKAGE="$BUILD_DIRECTORY/elsewhere-$VERSION.deb"
cd "$SOURCE_DIRECTORY"
dpkg-deb --build elsewhere
mv elsewhere.deb "$PACKAGE"

if $INSTALL ; then
    sudo dpkg -i "$PACKAGE"
fi
