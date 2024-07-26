#!/usr/bin/env python3

"""
A script to print a custom Message of the Day (MOTD) in Termux.
It includes the current date and time, a random quote, a random header, device information, and dynamic elements.
"""

import sys
import os
from datetime import datetime

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import load_items, get_random_item, get_device_info, get_battery_status, get_storage_usage
from src.config import QUOTES_FILE, HEADERS_FILE

def print_motd() -> None:
    """
    Print a custom Message of the Day (MOTD) in Termux.
    """
    # Load quotes and headers from files
    quotes = load_items(QUOTES_FILE)
    headers = load_items(HEADERS_FILE)

    # Print the MOTD
    print("Welcome to Termux!")
    print(f"Today is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Have a great day!")
    print("Here's a random quote for you:")
    print(get_random_item(quotes))
    print("Here's a random header for you:")
    print(get_random_item(headers))
    print(get_device_info())  # Display device information
    print(get_battery_status())  # Display battery status
    print(get_storage_usage())  # Display storage usage

if __name__ == "__main__":
    print_motd()

