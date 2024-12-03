import yaml
import os


def read_yaml(file_path):
    """Read and parse the YAML file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{os.path.abspath(file_path)} was not found.")
    else:
        with open(file_path, "r") as file:
            return yaml.safe_load(file)
