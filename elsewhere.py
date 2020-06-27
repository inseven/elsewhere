#!/usr/bin/env python3

import atexit
import logging
import os
import signal
import subprocess
import sys
import threading

import gpiozero

import RPi.GPIO as GPIO


GPIO_PIN = 17

URLS = [
#    "https://www.ustream.tv/embed/9408562?html5ui",
    "https://www.youtube.com/watch?v=nQZ5gGKmwNk",
    "https://www.youtube.com/watch?v=IcWTPFnqOLo",
    "https://www.youtube.com/watch?v=F109TZt3nRc"
]


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')


def livestreamer(url):
    env = {
        **os.environ,
        "DISPLAY": ":0.0",
    }
    return subprocess.Popen(["livestreamer", "--player", "vlc --fullscreen", url, "best"], env=env)


class Streamer(threading.Thread):

    def run(self):
        while True:
            livestreamer(URLS[0]).wait()
            

class Player(object):

    def __init__(self, urls):
        self.process = None
        self.urls = urls
        self.index = 0

    def play(self):
        if self.process is not None:
            self.process.terminate()
        url = self.url
        logging.info(f"Playing {url}...")
        self.process = livestreamer(url)

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
    subprocess.check_call(["/sbin/reboot"])


def setup_buttons(commands):
    buttons = []
    for pin, command in commands.items():
        button = gpiozero.Button(pin)
        button.when_pressed = command
        buttons.append(button)
    return buttons


def main():
    thread = Streamer()
    thread.start()
    
    player = Player(urls=URLS)
    buttons = setup_buttons({
        17: shutdown,
        22: reboot,
        23: next_video(player),
        27: previous_video(player),
    })
    # player.play()
    signal.pause()


if __name__ == "__main__":
    main()
