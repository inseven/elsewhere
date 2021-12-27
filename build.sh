#!/usr/bin/env bash

set -e
set -o pipefail
set -u

font="fonts/Inter/static/Inter-Thin.ttf"

echo "Generating splash screens..."
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" splash/splash.png
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 32 -gravity center label:"Shutting Down..." splash/shutting-down.png

# Build the Debian package.
echo "Building Debian package..."
cd package
dpkg-deb --build elsewhere
