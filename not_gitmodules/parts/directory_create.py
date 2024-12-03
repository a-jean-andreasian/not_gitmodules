import os


def ensure_dir_exists(directory):
    """Ensures the directory exists."""
    os.makedirs(directory, exist_ok=True)
