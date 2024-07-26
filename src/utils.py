import subprocess
import os

def load_items(file_path: str) -> list[str]:
    """Load items from a file and return as a list of strings."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_item(items: list[str]) -> str:
    """Return a random item from a list of strings."""
    return random.choice(items)

def get_command_output(command: str) -> str:
    """Execute a command and return its output as a string."""
    return subprocess.check_output(command.split()).decode().strip()

def get_device_info() -> str:
    """Return device information using Termux-API commands."""
    return f"Device Info: {get_command_output('termux-info')}"

def get_battery_status() -> str:
    """Return battery status using Termux-API commands."""
    return f"Battery Status: {get_command_output('termux-battery-status')}"

def get_storage_usage() -> str:
    """Return storage usage information."""
    return f"Storage Usage: {get_command_output('df -h')}"

