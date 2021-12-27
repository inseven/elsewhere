#!/usr/bin/env bash

set -e
set -o pipefail
set -u

font="fonts/Inter/static/Inter-Thin.ttf"

SPLASH_BUILD_DIRECTORY=package/elsewhere/usr/share/elsewhere/splash/images

echo "Generating splash screens..."
mkdir -p "$SPLASH_BUILD_DIRECTORY"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" "$SPLASH_BUILD_DIRECTORY/splash.png"
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 32 -gravity center label:"Shutting Down..." "$SPLASH_BUILD_DIRECTORY/shutting-down.png"

# Build the Debian package.
echo "Building Debian package..."
cd package
dpkg-deb --build elsewhere
