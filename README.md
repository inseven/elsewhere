# Elsewhere

Raspberry Pi based picture frame intended for displaying livestreams.

## Parts

- [LG LP097QX1 - iPad 3/4 Retina Display](https://www.adafruit.com/product/1751)

## Notes

```bash
chromium-browser --app="https://www.youtube.com/embed/hmtqztrfvE4?start=0&autoplay=1&mute=1" --start-fullscreen
```

If you're running over an SSH session, it may be necessary to set the `DISPLAY` environment variable:

```bash
DISPLAY=:0.0 chromium-browser --app="https://www.youtube.com/embed/hmtqztrfvE4?start=0&autoplay=1&mute=1" --start-fullscreen
```

Configure this to run on boot, by adding the following to `~/.config/autostart/youtube.desktop`:

```ini
[Desktop Entry]

Type=Application
Name=YouTube
Exec=chromium-browser --app="https://www.youtube.com/embed/hmtqztrfvE4?start=0&autoplay=1&mute=1" --start-fullscreen
```
