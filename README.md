# Elsewhere

Raspberry Pi based picture frame intended for displaying livestreams.

![Render](images/render.png)

## Parts

| **Part**                             | **Store**                                               | **Price**         |
| ------------------------------------ | ------------------------------------------------------- | ----------------- |
| Raspberry Pi Zero W                  | [Adafruit](https://www.adafruit.com/product/3400)       | $10.00            |
| Pimoroni HDMI 10" IPS LCD Screen Kit | [Adafruit](https://www.adafruit.com/product/4337)       | $139.95           |
| Picture Frame Hook                   | [Amazon](https://www.amazon.com/gp/product/B07GLCXVZZ/) | $10.99 (for 200)  |
| USB-C Panel Mount                    | [eBay](https://www.ebay.com/itm/143134180140)           | $6.29             |
| USB-C to Micro USB Adapter           | [Amazon](https://www.amazon.com/gp/product/B07GH5KJH2/) | $6.99             |
| Micro USB Splitter Cable             | [Amazon](https://www.amazon.com/gp/product/B017OPOG58/) | $6.79             |
| HDMI Ribbon Cable (30 cm)            | [Adafruit](https://www.adafruit.com/product/3562)       | $2.75             |
| HDMI Plug Adapter                    | [Adafruit](https://www.adafruit.com/product/3548)       | $6.50             |
| Mini HDMI Plug Adapter               | [Adafruit](https://www.adafruit.com/product/3552)       | $6.50             |

## Installation

```bash
mkdir -p ~/projects
cd ~/projects
git clone git@github.com:jbmorley/elsewhere.git
cd elsewhere
python3 setup.py
```

To run Elsewhere on startup, add the following to your crontab:

```
@reboot /usr/bin/python3 /home/pi/projects/elsewhere/elsewhere.py /home/pi/projects/elsewhere/urls.txt
```

## Configuration

- **Device Orientation**

  If you would like to use the device upside down, you can flip the screen by adding `display_rotate=2` to `/boot/config.txt`. You will need to reboot after doing this.
