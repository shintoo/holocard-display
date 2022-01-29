"""
repository.py
Retrieve absolute paths to videos using NFC device data.

Project: holocard-display
Author: Sean Rapp
Date: 01-29-2022
"""

from mfrc522 import SimpleMFRC522

root_path = "/home/pi/Documents/Projects/holocard-display/holocard_display/repository/"
id_fname_map = {
        "holocard-display:sts-orbiter": "orbiter.mkv",
        "holocard-display:ingenuity": "ingenuity.mkv",
        "holocard-display:tiefighter": "tiefighter.mkv",
}

def get_path_from_id(identifier):
    """
    Get an absolute path for a video using an identifier.

    Args:
        identifier (str): Identifier for video

    Returns:
        str: Absolute path to video

    """

    if not identifier in id_fname_map:
        message = f"Attempted to retrieve filepath for invalid ID:\nQuery: '{identifier}'"
        message += f"\nAvailable IDs:\n{list(id_fname_map.keys())}"
        print(message)
        raise ValueError(message)

    path = root_path + id_fname_map[identifier]
    return path


def write_repository_to_tags(num_tags):
    """
    Interface for writing out the repository's IDs to a series
    of NFC tags.

    Args:
        num_tags (int): Number of tags to write

    """
    ids = list(id_fname_map.keys())
    reader = SimpleMFRC522()

    for i in range(num_tags):
        tag_number = i + 1
        for t in enumerate(ids):
            print(f"{t[0]}: {t[1]}")

        print()
        id_index_to_write = int(input(f"Enter number of ID to write to tag #{tag_number}: "))
        id_to_write = ids[id_index_to_write]
        print(f"Tap tag #{tag_number}")
        reader.write(id_to_write)
        print(f"Successfully wrote '{id_to_write}' to tag #{tag_number}")
        ids.remove(id_to_write)

