#!/usr/bin/env python3

"""
A script to print a custom Message of the Day (MOTD) in Termux.
It includes the current date and time, a random quote, a random header, device information, and dynamic elements.
"""

import datetime
import random
import subprocess
import os

# Load quotes and headers from external files
def load_items(file_path: str) -> list:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

QUOTES = load_items(os.path.expanduser("~/.termux-rad-motd/quotes.txt"))
HEADERS = load_items(os.path.expanduser("~/.termux-rad-motd/headers.txt"))

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

def get_battery_status() -> str:
    """
    Returns battery status using Termux-API commands.
    """
    battery_status_cmd = "termux-battery-status"
    battery_status = subprocess.check_output(battery_status_cmd.split()).decode().strip()
    return f"Battery Status: {battery_status}"

def get_storage_usage() -> str:
    """
    Returns storage usage information.
    """
    storage_usage_cmd = "df -h"
    storage_usage = subprocess.check_output(storage_usage_cmd.split()).decode().strip()
    return f"Storage Usage: {storage_usage}"

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
    print(get_battery_status())  # Display battery status
    print(get_storage_usage())  # Display storage usage

if __name__ == "__main__":
    print_motd()

