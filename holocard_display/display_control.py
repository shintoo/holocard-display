"""
display_control.py
Enabling, disabling, and controlling display output.

Project: holocard-display
Author: Sean Rapp
Date: 01-29-2022
"""
import subprocess
from multiprocessing import Process, Event

display = "HDMI"

test_enabled = False

def check_display_enabled():
    """Returns True if the display is enabled, False otherwise."""
    global test_enabled
    return test_enabled
    #xr = subprocess.run(["xrandr", "-q"], capture_output=True)

    #return display.encode() + b" connected" in xr.stdout

def enable_display():
    """Enable the display (turn it on)"""
    global test_enabled
    test_enabled = True
    #subprocess.run(["xrandr", display, "<opts>"])
    print("xrandr <display> <opts>")

def disable_display():
    """Disable the display (turn it off)"""
    global test_enabled
    test_enabled = False
    #subprocess.run(["xrandr", display, "--off"])
    print("xrandr <display> --off")

def start_video(filepath):
    """
    Kill any running MPV processes and start a new one.

    Args:
        filepath (str): The path of the video to play

    """
    if not check_display_enabled():
        enable_display()

    # Kill current mpv process
    #subprocess.run(["pkill", "mpv"])
    print("pkill mpv")
    # Start new mpv using file
    #subprocess.run(["mpv", filepath, "--loop", inf"])
    print(f"mpv {filepath} --loop inf")
