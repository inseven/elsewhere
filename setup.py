#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess


SCRIPT_PATH = os.path.realpath(__file__)
ROOT_DIRECTORY = os.path.dirname(SCRIPT_PATH)
AUTOSTART_DIRECTORY = os.path.expanduser("~/.config/autostart")

LOGS_DIRECTORY = os.path.expanduser("~/Logs")
LOGS_PATH = os.path.join(LOGS_DIRECTORY, "elsewhere.log")

ELSEWHERE_FILENAME = "elsewhere.py"
DESKTOP_ENTRY_FILENAME = "elsewhere.desktop"

DESKTOP_ENTRY_TEMPLATE = """
[Desktop Entry]

Type=Application
Name=Elsewhere
Exec=/bin/bash -c "%s %s >> %s 2>&1"
"""


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')


def makedirs(path):
    if os.path.exists(path):
        return
    logging.info("Creating '%s'...")
    os.makedirs(path)


def main():
    parser = argparse.ArgumentParser(description="Configure Elsewhere to run on startup.")
    parser.add_argument("streams", help="URL containing new-line separated livestream URLs")
    options = parser.parse_args()

    logging.info("Installing livestreamer...")
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "livestreamer"])

    makedirs(AUTOSTART_DIRECTORY)
    makedirs(LOGS_DIRECTORY)

    desktop_entry_path = os.path.join(AUTOSTART_DIRECTORY, DESKTOP_ENTRY_FILENAME)
    logging.info("Creating '%s'...", desktop_entry_path)
    with open(desktop_entry_path, "w") as fh:
        desktop_entry = DESKTOP_ENTRY_TEMPLATE % (os.path.join(ROOT_DIRECTORY, ELSEWHERE_FILENAME),
                                                  options.streams,
                                                  LOGS_PATH)
        fh.write(desktop_entry)


if __name__ == "__main__":
    main()
