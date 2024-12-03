import shutil


def move_folder(path, destination):
    """
    ** Withdrawn function:
        Move a folder to a new destination.
    """
    try:
        shutil.move(path, destination)
        print(f"Successfully moved {path} to {destination}.")
    except Exception as e:
        print(f"Error occurred while moving {path} to {destination}: {e}")
