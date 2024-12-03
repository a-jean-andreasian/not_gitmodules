import os, shutil, stat
import subprocess


def delete_using_subprocess(path):
    subprocess.run(["rm", path, "-r", "-f" ], check=True)


def drop_read_only(path):
    try:
        os.chmod(path, stat.S_IWRITE)
    except PermissionError:
        delete_using_subprocess(path)


def delete_git_folder(directory):
    """Deletes .git folder from a directory"""
    git_folder_path = os.path.join(directory, '.git')

    if os.path.exists(git_folder_path):
        try:
            shutil.rmtree(git_folder_path)
        except PermissionError:
            drop_read_only(git_folder_path)
            shutil.rmtree(git_folder_path)
