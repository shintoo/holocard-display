holocard-display

Controls video playback on a display using NFC tags.

[render1](assets/mockup/forward-housing.png)
[render2](assets/mockup/reverse-no-housing.png)

I use this for what is basically a desk toy; several NFC cards are labelled with different
spacecraft, and a simple "hologram" is made with the display using a CD case cover glass.
Tapping the NFC cards on the device changes the hologram to display the spacecraft on
the card.

setup
=====
The SPI kernel module must be enabled to use the SPI drivers with the MFRC522.
On an RPI, this can be enabled using the following steps:

1. sudo raspi-config
2. Select Interface Options
3. Select SPI
4. Select Yes
5. Select OK
6. Select Finish
7. sudo reboot
8. lsmod | grep spi
9. Verify spi_bcm2835 is available

If this was not successful, edit /boot/config.txt to uncomment the `dtparam=spi=on` line.

Following this, install this repo:
$ git clone https://github.com/shintoo/holocard-display.git
$ cd holocard-display
$ python -m pip install .

Update root_path in holocard_display/repository.py to your installed location (or wherever
you wish to move the assets to, e.g. ~/.holocard

To write the NFC cards, pass `--write_tags <num cards>`
To run the display, omit this option.
If 2Hz is too slow for you for the NFC module polling, the poll
rate can be changed with `--poll_rate <rate in Hz>`

This does rely on a running X session (set up required if your rpi is headless), and
the video player `mpv`:

$ sudo apt install mpv

h/w
===

needed:
- 1 rpi (4b is used but anything after 1B+ should have the same pinout)
- 1 rc522 module
- 1 switch
- 1 pull down resistor
- 1 micro hdmi display
- x nfc tags
optional:
- cd case cover glass
- cardboard
- privacy screen 'protector'

Connection setup (using GPIO.BOARD indexing):
```
+=============+
| rpi   rc522 |
|-------------|
| 1     3v3   |
| 6     gnd   |
| 19    mosi  |
| 21    miso  |
| 22    rst   |
| 23    sck   |
| 24    sda   |
|-------------|
| 17    pd res|
| 36    switch|
+=============+
```
And of course the display connected via the micro hdmi port.

In summary:
 - an NFC module is connected for reading and writing NFC cards
 - A display is connected in order to... display
 - A switch is connected for turning on/off the display (using xrandr)
 - Write video IDs to the NFC cards using --write_tags <num tags>
 - Run the display and tap NFC cards to change the running video
