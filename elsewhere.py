#!/usr/bin/env python3

import argparse
import atexit
import logging
import os
import re
import signal
import subprocess
import sys
import threading

import gpiozero
import requests


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')


def livestreamer(url):
    env = {
        **os.environ,
        "DISPLAY": ":0.0",
    }
    return subprocess.Popen(["livestreamer", "--player", "vlc --fullscreen", url, "best"], env=env)


class Streamer(threading.Thread):

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.lock = threading.Lock()
        self._should_stop = False
        self.process = None

    def run(self):
        while True:
            process = None
            with self.lock:
                if self._should_stop:
                    return
                else:
                    process = livestreamer(self.url)
                    self.process = process
            process.wait()

    def stop(self):
        with self.lock:
            self._should_stop = True
            self.process.terminate()
        self.join()


class Player(object):

    def __init__(self, urls):
        self.streamer = None
        self.urls = urls
        self.index = 0

    def play(self):
        if self.streamer is not None:
            self.streamer.stop()
        url = self.url
        logging.info(f"Playing {url}...")
        self.streamer = Streamer(url=url)
        self.streamer.start()

    def next(self):
        self.index = (self.index + 1) % len(self.urls)

    def previous(self):
        self.index = (self.index - 1) % len(self.urls)

    @property
    def url(self):
        return self.urls[self.index]


def next_video(player):
    def inner():
        player.next()
        player.play()
    return inner


def previous_video(player):
    def inner():
        player.previous()
        player.play()
    return inner


def shutdown():
    subprocess.check_call(["sync"])
    subprocess.check_call(["/sbin/shutdown", "-h", "now"])


def reboot():
    subprocess.check_call(["sync"])
    subprocess.check_call(["sudo", "/sbin/reboot"])


def setup_buttons(commands):
    buttons = []
    for pin, command in commands.items():
        button = gpiozero.Button(pin)
        button.when_pressed = command
        buttons.append(button)
    return buttons


def main():
    parser = argparse.ArgumentParser(description="Livestream picture frame software.")
    parser.add_argument("streams", help="URL containing new-line separated livestream URLs")
    options = parser.parse_args()
    response = requests.get(options.streams)
    lines = [re.sub(r"(#.+)", "", line.strip()) for line in response.text.split("\n")]
    urls = [line for line in lines if line]
    player = Player(urls=urls)
    buttons = setup_buttons({
        21: shutdown,
        22: reboot,
        20: next_video(player),
        16: previous_video(player),
    })
    player.play()
    signal.pause()


if __name__ == "__main__":
    main()
