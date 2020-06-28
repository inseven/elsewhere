# Elsewhere

Raspberry Pi based picture frame intended for displaying livestreams.

## Parts

- [LG LP097QX1 - iPad 3/4 Retina Display](https://www.adafruit.com/product/1751)

## Installation

```bash
git clone git@github.com:jbmorley/elsewhere.git
cd elsewhere
python3 setup.py
```

## Configuration

The Raspberry Pi Zero seems to be unable to detect the resolution of an iPad 3 display correctly, requiring explicit configuration in `/boot/config.txt`:

```
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
#disable_overscan=1
hdmi_drive=1
hdmi_ignore_edid=0xa5000080
hdmi_group=2
hdmi_mode=87
#60Hz
hdmi_pixel_freq_limit=206000000
hdmi_timings=2048 0 150 5 5 1536 0 3 1 9 0 0 0 60 0 205210000 1
max_framebuffer_width=2048
max_framebuffer_height=1536
display_rotate=0
framebuffer_width=2048
framebuffer_height=1536
```

See https://github.com/area515/Photonic3D/issues/286 for more details.
