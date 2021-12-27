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

# Install Python dependencies
pip3 install -r requirements.txt

# Install the service
sudo atx-monitor/atx-monitor install

# Initial urls.txt configuration.
# echo "ustream.tv/channel/iss-hdev-payload" > /home/pi/projects/elsewhere/urls.txt
