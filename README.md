# Elsewhere

Raspberry Pi based picture frame intended for displaying livestreams.

## Parts

- [LG LP097QX1 - iPad 3/4 Retina Display](https://www.adafruit.com/product/1751)

## Notes

```bash
livestreamer --player "vlc --fullscreen" "https://www.youtube.com/watch?v=nQZ5gGKmwNk" best
```

If you're running over an SSH session, it may be necessary to set the `DISPLAY` environment variable:

```bash
DISPLAY=:0.0 livestreamer --player "vlc --fullscreen" "https://www.youtube.com/watch?v=nQZ5gGKmwNk" best
```

Configure this to run on boot, by adding the following to `~/.config/autostart/youtube.desktop`:

```ini
[Desktop Entry]

Type=Application
Name=YouTube
Exec=livestreamer --player "vlc --fullscreen" "https://www.youtube.com/watch?v=nQZ5gGKmwNk" best
```

_The documentation on [SparkFun](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup/all) was useful when working out the best way to run applications on startup._

```

```
