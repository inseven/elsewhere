#!/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import sys
import time

import RPi.GPIO as GPIO

import jinja2

import cli


ROOT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIRECTORY = os.path.join(ROOT_DIRECTORY, "atx-monitor")

SERVICE_NAME = "atx-monitor.service"

ATX_MONITOR_PATH = os.path.join(ROOT_DIRECTORY, "atx-monitor", "atx-monitor")
SERVICE_PATH = os.path.join("/etc/systemd/system", SERVICE_NAME)

REBOOT_MINIMUM_DURATION = 0.2
REBOOT_MAXIMUM_DURATION = 2.0


verbose = '--verbose' in sys.argv[1:] or '-v' in sys.argv[1:]
logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO, format="[%(levelname)s] %(message)s")


@cli.command("install")
def command_install(options):
    logging.info("Installing...")

    environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_DIRECTORY))
    template = environment.get_template("atx-monitor.service")

    with open(SERVICE_PATH, "w") as fh:
        fh.write(template.render(path=ATX_MONITOR_PATH))

    logging.info("Reloading systemd...")
    subprocess.check_call(["systemctl", "daemon-reload"])

    logging.info("Enabling and starting service...")
    subprocess.check_call(["systemctl", "enable", SERVICE_NAME])
    subprocess.check_call(["systemctl", "start", SERVICE_NAME])

    logging.info("Done.")


@cli.command("log")
def command_log(options):
    subprocess.run(["journalctl", "-u", SERVICE_NAME, "-f"])


def wait_for_low(channel, maximum_duration):
    start = time.time()
    while True:
        logging.info("Waiting for low...")
        time.sleep(0.1)
        duration = time.time() - start
        if not GPIO.input(channel) or duration > maximum_duration:
            return duration


@cli.command("monitor")
def command_monitor(options):
    
    boot_ok = 8
    shutdown = 7

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(boot_ok, GPIO.OUT)
    GPIO.setup(shutdown, GPIO.IN)
    
    # Reset the board by toggling the the boot OK signal
    GPIO.output(boot_ok, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(boot_ok, GPIO.HIGH)

    while True:
        time.sleep(0.1)
        if GPIO.input(shutdown):
            logging.info("Received input...")
            duration = wait_for_low(shutdown, REBOOT_MAXIMUM_DURATION)
            if duration < REBOOT_MINIMUM_DURATION:
                logging.info("Ignoring unknown signal...")
                continue
            elif duration < REBOOT_MAXIMUM_DURATION:
                logging.info("Rebooting..")
                subprocess.check_call(["sudo", "reboot"])
                break
            else:
                logging.info("Shutting down...")
                subprocess.check_call(["sudo", "poweroff"])
                break

    # Note that we don't clean up the GPIO to ensure the boot OK signal remains high.
                

def main():
    parser = cli.CommandParser()
    parser.add_argument('--verbose', '-v', action='store_true', default=False, help="show verbose output")
    parser.run()


if __name__ == "__main__":
    main()
