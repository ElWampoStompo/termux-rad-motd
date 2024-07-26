import os
import random
import subprocess
from typing import List

# Constants for file paths
from .config import QUOTES_FILE, HEADERS_FILE

def load_items(file_path: str) -> List[str]:
    """
    Load items from a file and return as a list of strings.

    Args:
        file_path (str): Path to the file containing items.

    Returns:
        List[str]: List of items read from the file.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_item(items: List[str]) -> str:
    """
    Return a random item from a list of strings.

    Args:
        items (List[str]): List of items to choose from.

    Returns:
        str: Randomly selected item.
    """
    return random.choice(items)

def get_command_output(command: str) -> str:
    """
    Execute a command and return its output as a string.

    Args:
        command (str): Command to be executed.

    Returns:
        str: Output of the command.
    """
    result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
    return result.stdout.strip()

def get_file_content(file_path: str) -> str:
    """
    Return the content of a file as a single string.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()

def get_device_info() -> str:
    """
    Return device information using Termux-API commands.

    Returns:
        str: Device information.
    """
    return f"Device Info: {get_command_output('termux-info')}"

def get_battery_status() -> str:
    """
    Return battery status using Termux-API commands.

    Returns:
        str: Battery status.
    """
    return f"Battery Status: {get_command_output('termux-battery-status')}"

def get_storage_usage() -> str:
    """
    Return storage usage information.

    Returns:
        str: Storage usage information.
    """
    return f"Storage Usage: {get_command_output('df -h')}"

def get_random_quote() -> str:
    """
    Return a random quote from the quotes file.

    Returns:
        str: Randomly selected quote.
    """
    quotes = load_items(QUOTES_FILE)
    return get_random_item(quotes)

def get_header() -> str:
    """
    Return the header from the headers file.

    Returns:
        str: Header text.
    """
    headers = load_items(HEADERS_FILE)
    return headers[0] if headers else ""

