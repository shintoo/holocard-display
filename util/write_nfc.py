#!/usr/bin/env python3

from RPi import GPIO
from mfrc522 import SimpleMFRC522

def main(argv):
    reader = SimpleMFRC522()
    try:
        text = input("Enter NFC data: ")
        print(f"Place tag to write '{text}'")
        reader.write(text)
        print(f"Wrote '{text}'")
    except Exception as e:
        print(f"Error occurred during write: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    import sys
    main(sys.argv)
