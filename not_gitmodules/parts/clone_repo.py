import os
import subprocess


def clone_repo(root_dir_name, directory_name, url) -> bool | None:
    """Clone the repository into the specified directory."""
    target_path = os.path.join(root_dir_name, directory_name)

    # Skip if the target directory already exists
    if os.path.exists(target_path):
        print(f"Directory '{target_path}' already exists. Skipping...")
        return None

    print(f"Processing {directory_name} -> {url}")

    # Clone the repository to the base directory
    print(f"Cloning {url} into {target_path}...")
    try:
        subprocess.run(
            ["git", "clone", url, target_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        print(f"Successfully cloned to {target_path}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {url}: {e.stderr}")
    except FileExistsError:
        print(f"Target path {target_path} already exists.")
    else:
        return True
