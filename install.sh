#!/usr/bin/env bash

set -e
set -o pipefile

# Install package dependencies.
sudo apt-get update
sudo apt-get upgrade --yes
xargs -a /home/pi/projects/elsewhere/packages.txt sudo apt-get install --yes

# Enable unattended updates.
echo unattended-upgrades unattended-upgrades/enable_auto_updates boolean true | sudo debconf-set-selections
sudo dpkg-reconfigure -f noninteractive unattended-upgrades

# Initial urls.txt configuration.
echo "ustream.tv/channel/iss-hdev-payload" > /home/pi/projects/elsewhere/urls.txt


pip3 install -r requirements.txt

# Install the service
sudo atx-monitor/atx-monitor install


