"""
display_control.py
Enabling, disabling, and controlling display output.

Project: holocard-display
Author: Sean Rapp
Date: 01-29-2022
"""
import subprocess
from multiprocessing import Process, Event

def enable_display():
    """Enable the display (turn it on)"""
    #subprocess.run(["xrandr", "<display>", "<opts>"])
    print("xrandr <display> <opts>")

def disable_display():
    """Disable the display (turn it off)"""
    #subprocess.run(["xrandr", "<display>", "--off"])
    print("xrandr <display> --off")

def start_video(filepath):
    """
    Kill any running MPV processes and start a new one.

    Args:
        filepath (str): The path of the video to play

    """
    # Kill current mpv process
    #subprocess.run(["pkill", "mpv"])
    print("pkill mpv")
    # Start new mpv using file
    #subprocess.run(["mpv", filepath, "--loop", inf"])
    print(f"mpv {filepath} --loop inf")

