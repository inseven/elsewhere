#!/usr/bin/env python3

import subprocess


def youtube(identifier):
    return subprocess.run(["livestreamer", "--player", "vlc --fullscreen", "https://www.youtube.com/watch?v=%s" % (identifier, ), "best"])


def main():
    while True:
        youtube("nQZ5gGKmwNk")


if __name__ == "__main__":
    main()
