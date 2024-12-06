import os, shutil, stat
from pathlib import Path


def drop_read_only(path):
    try:
        os.chmod(path, stat.S_IWRITE)
    except PermissionError:
        ...


def delete_git_folder(directory):
    """Deletes .git folder from a directory"""
    git_folder_path = os.path.join(directory, ".git")

    if os.path.exists(git_folder_path):
        try:
            shutil.rmtree(git_folder_path)
        except PermissionError as err:
            read_only_fp = str(err).split('denied:')[1].strip().strip("'")
            p = Path(read_only_fp)
            drop_read_only(p)
            return delete_git_folder(directory)
        else:
            print(git_folder_path, 'was successfully deleted.')
