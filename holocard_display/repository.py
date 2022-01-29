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
    written_tag_ids = set()

    for i in range(num_tags):
        tag_number = i + 1
        print("Available IDs:")
        for t in enumerate(ids):
            print(f"  {t[0]}) {t[1]}")

        print()
        id_index_to_write = int(input(f"({tag_number}/{num_tags}) Enter number of ID to write to tag: "))
        id_to_write = ids[id_index_to_write]
        print(f"({tag_number}/{num_tags}) Tap tag to reader.")

        tag_id = reader.read_id()

        while tag_id in written_tag_ids:
            print(f"This tag (ID {tag_id}) has already been written to during this session.")
            confirm = input("Write anyway? [y/n]: ")
            if "y" in confirm.lower():    
                print(f"({tag_number}/{num_tags}) Tap tag to reader.") 
                break
            print("Tap a different tag.")
            tag_id = reader.read_id()

        written_id, written_data = reader.write(id_to_write)
        written_tag_ids.add(tag_id)
        print(f"Successfully wrote '{written_data}' to tag (ID {written_id})")
        ids.remove(id_to_write)
        written_tag_ids.add(written_id)

