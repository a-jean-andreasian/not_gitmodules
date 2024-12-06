from pathlib import Path
import shutil

LEFTOVER_FILES = '.gitignore', 'README.md', 'LICENSE'
LEFTOVER_FOLDERS = '.github',


def clean_github_leftovers(module_path):
    """
    Deletes files like .gitignore, README.md, LICENSE and folders like .github from the cloned module.
    """
    module_path = Path(module_path)

    for file_name in LEFTOVER_FILES:
        file_path = module_path / file_name
        if file_path.exists():
            file_path.unlink()

    for folder_name in LEFTOVER_FOLDERS:
        folder_path = module_path / folder_name
        if folder_path.exists() and folder_path.is_dir():
            shutil.rmtree(folder_path)

    print('Leftover files were successfully removed.')
