# Elsewhere

Raspberry Pi based picture frame for displaying livestreams.

![Elsewhere showing a livestream of Earth from the ISS](images/iss.jpg)

## Parts

| **Part**                             | **Link**                                                | Quantity | **Unit Price** | **Price** |
| ------------------------------------ | ------------------------------------------------------- | -------- | -------------- | --------- |
| Raspberry Pi Zero W                  | [Adafruit](https://www.adafruit.com/product/3400)       | 1        | $10.00         | $10.00    |
| Pimoroni HDMI 10" IPS LCD Screen Kit | [Adafruit](https://www.adafruit.com/product/4337)       | 1        | $139.95        | $139.95   |
| D-Ring Picture Hanger, M4            |                                                         | 2        |                |           |
| USB-C Panel Mount                    | [eBay](https://www.ebay.com/itm/143134180140)           | 1        | $6.29          | $6.29     |
| USB-C to Micro USB Adapter           | [Amazon](https://www.amazon.com/gp/product/B07GH5KJH2/) | 1        | $6.99          | $6.99     |
| Micro USB Splitter Cable             | [Amazon](https://www.amazon.com/gp/product/B017OPOG58/) | 1        | $6.79          | $6.79     |
| HDMI Ribbon Cable, 30 cm             | [Adafruit](https://www.adafruit.com/product/3562)       | 1        | $2.75          | $2.75     |
| HDMI Plug Adapter                    | [Adafruit](https://www.adafruit.com/product/3548)       | 1        | $6.50          | $6.50     |
| Mini HDMI Plug Adapter               | [Adafruit](https://www.adafruit.com/product/3552)       | 1        | $6.50          | $6.50     |
| M3 Standoffs, 10mm                   | [McMaster-Carr](https://www.mcmaster.com/94868A166/)    | 8        | $1.24          | $9.92     |

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

  To change the orientation of your device, add `display_rotate=2` to `/boot/config.txt` and reboot.0
