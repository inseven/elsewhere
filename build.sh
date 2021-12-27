#!/usr/bin/env bash

set -e
set -o pipefail
set -u

font="fonts/Inter/static/Inter-Thin.ttf"

convert -background black -fill white -font "$font" -size 1024x768 -pointsize 64 -gravity center label:"Elsewhere" splash/splash.png
convert -background black -fill white -font "$font" -size 1024x768 -pointsize 32 -gravity center label:"Shutting Down..." splash/shutting-down.png
