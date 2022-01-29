"""
nfc_listener.py
Listener that takes data and error handling callbacks and runs a
loop handling device reads at a specified poll rate.

Project: holocard-display
Author: Sean Rapp
Date: 01-28-2022
"""
from time import sleep

from mfrc522 import SimpleMFRC522
from RPi import GPIO

def nfc_listener(poll_rate, read_handler, error_handler):
    """
    Listens for NFC devices and executes the handler reading.

    Args:
        poll_rate (float): Rate in Hz at which to poll the NFC reader
        read_handler (Callable[id: int, data: str]): Function that is called upon an NFC device read
        error_handler (Callable[Exception]): Function that is called if an error occurs

    """
    read_delay = 1 / poll_rate
    nfc_reader = SimpleMFRC522()

    while True:
        try:
            sleep(read_delay)
            nfc_id, nfc_data = nfc_reader.read()
            read_handler(nfc_id, nfc_data)
        except KeyboardInterrupt as ki:
            print("\b\bStopping nfc_listener")
            break
        except Exception as e:
            error_handler(e)
            continue
