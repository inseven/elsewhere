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
import urllib.request

import gpiozero
import inkyphat
import requests

from flask import Flask, escape, request, jsonify


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')


def livestreamer(url):
    env = {
        **os.environ,
        "DISPLAY": ":0.0",
    }
    return subprocess.Popen(["livestreamer", "--player", "vlc --fullscreen", url, "best"], env=env)


app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


class Server(threading.Thread):

    def __init__(self, player, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.player = player
        def next():
            self.player.next()
            return jsonify({'url': self.player.url})
        def previous():
            self.player.previous()
            return jsonify({'url': self.player.url})
        def shutdown():
            self.player.shutdown()
            return jsonify({})
        def reboot():
            self.player.reboot()
            return jsonify({})
        app.add_url_rule('/api/v1/next', 'next', next)
        app.add_url_rule('/api/v1/previous', 'previous', previous)
        app.add_url_rule('/api/v1/shutdown', 'shutdown', shutdown)
        app.add_url_rule('/api/v1/reboot', 'reboot', reboot)

    def run(self):
        app.run(host='0.0.0.0')


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
        title = self.title
        logging.info("Setting title to '%s'...", title)
        inkyphat.set_colour("black")
        font = inkyphat.ImageFont.truetype(inkyphat.fonts.FredokaOne, 18)
        inkyphat.text((2, 2), title, 1, font=font)
        inkyphat.show()
        self.streamer = Streamer(url=url)
        self.streamer.start()

    def next(self):
        self.index = (self.index + 1) % len(self.urls)
        self.play()

    def previous(self):
        self.index = (self.index - 1) % len(self.urls)
        self.play()

    def shutdown(self):
        subprocess.run(["sudo", "shutdown", "-h", "now"])

    def reboot(self):
        subprocess.run(["sudo", "shutdown", "-r", "now"])

    @property
    def url(self):
        return self.urls[self.index][0]

    @property
    def title(self):
        details = self.urls[self.index]
        if len(details) > 1:
            return details[1]
        return ""


def next_video(player):
    def inner():
        player.next()
    return inner


def previous_video(player):
    def inner():
        player.previous()
    return inner


def shutdown():
    subprocess.check_call(["sync"])
    subprocess.check_call(["sudo", "/sbin/shutdown", "-h", "now"])


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
    parser.add_argument("--no-gpio", action="store_true", default=False, help="disable GPIO for channel controls")
    options = parser.parse_args()
    content = None
    if os.path.exists(options.streams):
        with open(options.streams, "r") as fh:
            content = fh.read()
    else:
        response = requests.get(options.streams)
        content = response.text
    lines = [re.sub(r"(#.+)", "", line.strip()) for line in content.split("\n")]
    urls = [line.split(" ", 1) for line in lines if line]
    player = Player(urls=urls)
    if not options.no_gpio:
        logging.info("Setting up GPIO buttons...")
        buttons = setup_buttons({
            21: shutdown,
            22: reboot,
            20: player.next,
            16: previous_video(player),
        })
    else:
        logging.info("Skipping GPIO button setup...")

    logging.info("Starting server...")
    server = Server(player=player)
    server.start()
        
    player.play()
    signal.pause()


if __name__ == "__main__":
    main()
