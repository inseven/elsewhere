#!/usr/bin/env bash

sudo apt-get update
xargs -a packages.txt sudo apt-get install --yes
