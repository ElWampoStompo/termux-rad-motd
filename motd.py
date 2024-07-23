#!/usr/bin/env python3

"""
A script to print a custom Message of the Day (MOTD) in Termux.
It includes the current date and time, a random quote, a random header, device information, and dynamic elements.
"""

import datetime
import random
import subprocess

QUOTES = [
    "Quote 1",
    "Quote 2",
    "Quote 3"
]

HEADERS = [
    "Header 1",
    "Header 2",
    "Header 3"
]

def get_random_item(items: list) -> str:
    """
    Returns a random item from a list.
    """
    return random.choice(items)

def get_device_info() -> str:
    """
    Returns device information using Termux-API commands.
    """
    device_info_cmd = "termux-info"
    device_info = subprocess.check_output(device_info_cmd.split()).decode().strip()
    return f"Device Info: {device_info}"

def print_motd() -> None:
    """
    Prints a custom Message of the Day (MOTD) in Termux.
    It includes the current date and time, a random quote, a random header, device information, and dynamic elements.
    """
    print("Welcome to Termux!")
    print(f"Today is {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Have a great day!")
    print("Here's a random quote for you:")
    print(get_random_item(QUOTES))
    print("Here's a random header for you:")
    print(get_random_item(HEADERS))
    print(get_device_info())  # Display device information

if __name__ == "__main__":
    print_motd()