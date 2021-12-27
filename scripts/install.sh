#!/usr/bin/env bash

set -e
set -o pipefail
set -u

# Install package dependencies.
sudo apt-get update
sudo apt-get upgrade --yes

# Enable unattended updates.
echo unattended-upgrades unattended-upgrades/enable_auto_updates boolean true | sudo debconf-set-selections
sudo dpkg-reconfigure -f noninteractive unattended-upgrades
