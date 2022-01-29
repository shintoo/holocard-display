#!/usr/bin/env python3
"""
holocard_display.py
Listens for NFC device taps and plays videos based on the data contained on the device.

Project: holocard-display
Author: Sean Rapp
Date: 01-29-2022
"""
from RPi import GPIO

from holocard_display.nfc_listener import nfc_listener
from holocard_display.nfc_handlers import nfc_read_handler, nfc_error_handler 
from holocard_display.repository import write_repository_to_tags
from holocard_display import display_control



def configure_io():
    """Configure board indexing mode and setup display switch callbacks"""
    display_control_switch_pin = 36
    # Use board indexing for GPIO pin numbers
    GPIO.setmode(GPIO.BOARD)
    # Set control switch pin to input, use internal pull down resistor
    GPIO.setup(display_control_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def callback(channel):
        # Check for rising vs falling edge
        # Enable on rising
        if GPIO.input(channel) == GPIO.HIGH:
            display_control.enable_display()
        # Disable on falling
        else:
            display_control.disable_display()

    # Add callback for both rising and falling edges on display switch pin
    GPIO.add_event_detect(
            display_control_switch_pin,
            GPIO.BOTH,
            callback=callback,
            bouncetime=100
    )


def start_display(argv):
    """Starts the display"""
    poll_rate = 2

    print("Starting holocard-display")

    try:
        configure_io()
        pass
    except Exception as e:
        print(f"Error during board configuration: {e}")
        print("Quitting due to error")
        return
    
    # Start the NFC listener
    nfc_listener(poll_rate, nfc_read_handler, nfc_error_handler)

    print("Quitting holocard-display")


def main(argv):
    if "--write_tags" in argv:
        try:
            num_tags = int(argv[argv.index("--write_tags") + 1])
            write_repository_to_tags(num_tags)
        except Exception as e:
            print(f"Error writing NFC tags: {e}")
            return

        print("Completed writing NFC tags")
        return

    if "--poll_rate" in argv:
        try:
            poll_rate = float(argv[argv.index("--poll_rate") + 1])
        except:
            print("Defaulting to poll rate of 2Hz")

    start_display(argv)


if __name__ == "__main__":
    try:
        import sys
        main(sys.argv)
    except Exception as e:
        print(f"Error during execution: {e}")

    GPIO.cleanup()