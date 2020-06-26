# Elsewhere

Raspberry Pi based picture frame intended for displaying livestreams.

## Parts

- [LG LP097QX1 - iPad 3/4 Retina Display](https://www.adafruit.com/product/1751)

## Installation

Configure to run on boot, by adding the following to `~/.config/autostart/elsewhere.desktop`:

```ini
[Desktop Entry]

Type=Application
Name=Elsewhere
Exec=/home/pi/Projects/elsewhere/elsewhere.py
```
