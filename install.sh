#!/usr/bin/env bash

# Install package dependencies.
sudo apt-get update
xargs -a packages.txt sudo apt-get install --yes

# Enable unattended updates.
echo unattended-upgrades unattended-upgrades/enable_auto_updates boolean true | sudo debconf-set-selections
sudo dpkg-reconfigure -f noninteractive unattended-upgrades
