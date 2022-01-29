"""
nfc_handlers.py
Handlers for reading and errors from NFC devices for holocard-display

Project: holocard-display
Author: Sean Rapp
Date: 01-29-2022
"""

from time import sleep
import subprocess

from holocard_display.repository import get_path_from_id
from holocard_display.display_control import enable_display, start_video

current_playing_id = None

def nfc_read_handler(nfc_id, nfc_data):
    """
    Handle read NFC holo IDs and start the display.
    Finds the filepath of the video to play from the NFC data.
    Kills the current running mpv process and starts a new one.

    Args:
        nfc_id (int): ID of the NFC device read
        nfc_data (str): Data read from the NFC device

    """
    global current_playing_id

    # Trim whitespace
    cleaned_data = nfc_data.strip()

    # Check that video needs to be changed
    if cleaned_data == current_playing_id:
        print("Same ID as currently playing, doing nothing")
        return

    # Get filepath from data -> filepath map
    try:
        filepath = get_path_from_id(cleaned_data)
    except ValueError as ve:
        print(f"Error in nfc_read_handler: {ve}")
        return

    start_video(filepath)

    current_playing_id = cleaned_data

def nfc_error_handler(exception):
    """
    Error handler for NFC device read errors.

    Args:
        exception (Exception): Exception to handle

    """
    print(f"Error during NFC read: {exception}")
