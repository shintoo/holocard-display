#!/usr/bin/env python3

from time import sleep

from RPi import GPIO
from mfrc522 import SimpleMFRC522

def main(argv):
    loop = "loop" in argv or "l" in argv

    reader = SimpleMFRC522()

    while True:
        try:
            print("Tap NFC device")
            nfc_id, text = reader.read()
            print(f"NFC read:\n\tID: '{nfc_id}'\n\tData: '{text}'")
        except KeyboardInterrupt:
            print("\b\bQuitting")
            break
        except Exception as e:
            print(f"Error occurred during read: {e}")

        if not loop:
            break

        sleep(0.5)

    GPIO.cleanup()

if __name__ == "__main__":
    import sys
    main(sys.argv)
