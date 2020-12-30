#!/usr/bin/env python3

import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description="Configure Elsewhere to run on startup.")
    parser.add_argument("streams", help="URL containing new-line separated livestream URLs")
    options = parser.parse_args()

    subprocess.run(["sudo", "apt-get", "update"])
    subprocess.run(["sudo",
                    "apt-get", "install",
                    "livestreamer",
                    "python3-bs4",
                    "python3-gpiozero",
                    "python3-flask"])


if __name__ == "__main__":
    main()
