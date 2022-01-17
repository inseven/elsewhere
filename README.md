# Elsewhere

[![Build](https://github.com/inseven/elsewhere/actions/workflows/build.yaml/badge.svg)](https://github.com/inseven/elsewhere/actions/workflows/build.yaml)

Raspberry Pi based picture frame for displaying livestreams.

![Render of the current Elsewhere design](images/hero.png)

## Parts

| **Part**                                  | **Link**                                                     | Quantity | **Unit Price**            | **Price**   |
| ----------------------------------------- | ------------------------------------------------------------ | -------- | ------------------------- | ----------- |
| **Raspberry Pi Zero 2 W**                 | [Adafruit](https://www.adafruit.com/product/5291) | 1        | $15.00                   | $15.00     |
| **Pimoroni HDMI 10" IPS LCD Screen Kit**  | [Adafruit](https://www.adafruit.com/product/4337)            | 1        | $139.95                   | $139.95     |
| HDMI Ribbon Cable, 30 cm                  | [Adafruit](https://www.adafruit.com/product/3562)            | 1        | $2.75                     | $2.75       |
| HDMI Plug Adapter                         | [Adafruit](https://www.adafruit.com/product/3548)            | 1        | $6.50                     | $6.50       |
| Mini HDMI Plug Adapter                    | [Adafruit](https://www.adafruit.com/product/3552)            | 1        | $6.50                     | $6.50       |
| **ATXRaspi R3**                           | [LowPowerLab](https://lowpowerlab.com/shop/product/91)       | 1        | $17.95                    | $17.95      |
| Jumper Wire | [LowPowerLab](https://lowpowerlab.com/shop/product/154) | 4 | $0.74 ($2.95 for 4) | $2.95 |
| D-Ring Picture Hanger, M4                 |                                                              | 2        |                           |             |
| USB-C Panel Mount                         | [eBay](https://www.ebay.com/itm/143134180140)                | 1        | $6.29                     | $6.29       |
| USB-C to Micro USB Adapter                | [Amazon](https://www.amazon.com/gp/product/B07GH5KJH2/)      | 1        | $6.99                     | $6.99       |
| Micro USB Splitter Cable                  | [Amazon](https://www.amazon.com/gp/product/B017OPOG58/)      | 1        | $6.79                     | $6.79       |
| microSD Card, 32GB                        | [Amazon](https://www.amazon.com/SAMSUNG-Select-microSDXC-Adapter-MB-ME128HA/dp/B06XWN9Q99) | 1        | $7.99                     | $7.99       |
| Female to Female Dupont Wire, 30cm | [Amazon](https://www.amazon.com/dp/B07GD1W1VL) | 6 | $0.08 ($8.99 for 120) | $0.48 |
| M3 Standoff, 10mm                         | [McMaster-Carr](https://www.mcmaster.com/94868A166/)         | 8        | $1.24                     | $9.92       |
| 4-40 Socket Head Screw, Low-Profile, 1/4" | [McMaster-Carr](https://www.mcmaster.com/93615A110/)         | 2        | $1.55 (Pack of 10)        | $3.10       |
| M3 Socket Head Screw, Low-Profile, 12mm   | [McMaster-Carr](https://www.mcmaster.com/92855A313/)         | 8        | $0.11 (Pack of 25)        | $0.22       |
| M3 Socket Head Screw, Low-Profile, 6mm    | [McMaster-Carr](https://www.mcmaster.com/92855A307/)         | 8        | $0.30 (Pack of 25)        | $0.60       |
| M2.5 Socket Head Screw, 6mm               | [McMaster-Carr](https://www.mcmaster.com/91292A010/)         | 18      | $0.06 ($6.00 for 100) | $1.08    |
| M2.5 Socket Head Screw, 4mm | [McMaster-Carr](https://www.mcmaster.com/91292A015/) | 18 | $0.30 ($7.43 for 25) | $5.40 |
| M2.5 Socket Head Screw, 10mm | [McMaster-Carr](https://www.mcmaster.com/91292A014/) | 2 | $0.07 ($6.54 for 100) | $0.14 |
| M2.5 Nut | [McMaster-Carr](https://www.mcmaster.com/91828A113/) | 2 | $0.08 ($7.18 for 100) | $0.16 |
| M2.5 Washer, 0.5mm | [McMaster-Carr](https://www.mcmaster.com/98689A111/) | 6 | $0.03 ($2.57 for 100) | $0.18 |
| M4 Socket Head Screw, Low-Profile, Partially Threaded, 10mm | [McMaster-Carr](https://www.mcmaster.com/96970A111/) | 2 | $1.48 | $2.96 |
| M4 Washer, 0.8mm | [McMaster-Carr](https://www.mcmaster.com/93475A230/) | 2 | $0.04 ($3.14 for 100) | $0.08 |
| M4 Locknut | [McMaster-Carr](https://www.mcmaster.com/93625A150/) | 2 | $0.08 ($7.67 for 100) | $0.16 |
| M2.5 Standoff, 6mm                        | [Digi-Key](https://www.digikey.com/en/products/detail/970060154/732-12827-ND/9488531) | 18      | $0.34 ($16.95 for 50) | $6.12   |
| **Laser-Cut Parts** | [Ponoko](https://ponoko.com) |  |  | $118.99 |
| **Controller Board** | [Oshpark](https://oshpark.com/shared_projects/Cnb1DUgJ) | 1 | $3.49 ($10.45 for 3) | $3.49 |
| Micro SD to Micro SD Extension Cable, 25cm | [AliExpress](https://www.aliexpress.com/item/4001154489373.html) | 1 | $3.00 | $3.00 |
|                                           |                                                              |          |                           | **$375.74** |

## Installation

1. Install Raspberry Pi OS Lite (Bullseye).

2. Add the package repository to `/etc/apt/sources.list`:

   ```bash
   deb [trusted=yes] http://packages.inseven.co.uk/raspbian/ ./
   ```

3. Update the `dtoverlay` property in `/boot/config.txt` to:

   ```ini
   dtoverlay=vc4-fkms-v3d
   ```

   (See https://forums.raspberrypi.com/viewtopic.php?t=324835.)
   
4. Add `fbcon=map:2 disable_splash=1 ` to `/boot/cmdline.txt`.

   These changes are as follows:

   - `fbcon=map:2` – Redirects the console during boot to ensure it doesn't appear on the HDMI display.
   - `disable_splash=1` – Disable the boot splash screen.

5. Disable the Serial Port and SPI:

   ```bash
   sudo raspi-config
   ```

   - Disable Serial Port
     - Interface Options
     - Serial Port
     - Login Shell: No
     - Serial Port Hardware: No
   - Disable SPI
     - Interface Options
     - SPI
     - Enabled: No

6. Reboot:

   ```bash
   sudo reboot
   ```

7. Update and upgrade Raspbian, and install Elsewhere:

   ```bash
   sudo apt update
   sudo apt upgrade --yes
   sudo apt install elsewhere --yes
   ```

8. Assuming everything has gone to plan, Elsewhere should now be running.

#### Unattended Upgrades

1. Enable all [unattended upgrades](https://wiki.debian.org/UnattendedUpgrades) by uncommenting the following lines in `/etc/apt/apt.conf.d/50unattended-upgrades`:

   ```
   Unattended-Upgrade::Origins-Pattern {
           // ...
           "origin=Debian,codename=${distro_codename}-updates";
           "origin=Debian,codename=${distro_codename}-proposed-updates";
           // ..
   }
   ```

2. Reboot:

   ```bash
   sudo reboot
   ```

## Troubleshooting

### Device takes too long to shutdown and ATXRaspi doesn't cut power

- Re-enable the console by removing `fbcon=map:2` from `/boot/cmdline.txt`.
- Check the the shutdown logs; are any services taking a long time to stop?

### Tailscale doesn't takes too long to stop

Customise the Tailscale service to shorten the shutdown timeout:

- Override the service:

  ```bash
  sudo systemctl edit tailscaled.service
  ```

- Add the following section:

  ```
  [Service]
  TimeoutSec=5
  ```

## Builds

Elsewhere is an iterative project, meaning I've put together a number of prototypes along the way. The most recent one still has the 4:3 aspect ratio, and has been happily showing us views from the ISS for the last few months.

![Elsewhere showing a livestream of Earth from the ISS](images/iss.jpg)
