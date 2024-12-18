import os
from .parts import delete_git_folder, ensure_dir_exists, clone_repo, read_yaml, clean_github_leftovers
from concurrent.futures import ThreadPoolExecutor


def proceed_task(root_dir_name, directory_name, repo_url):
    """Packed-up collection of actions, to run in a separate thread."""
    ensure_dir_exists(root_dir_name)

    if clone_repo(root_dir_name=root_dir_name, directory_name=directory_name, url=repo_url):
        module_path = os.path.join(root_dir_name, directory_name)
        delete_git_folder(module_path)
        clean_github_leftovers(module_path)
    # skipping else to not perform clean-up on skipped directories


def execute_sequentially(root_dir_name: str, repo_dict: dict):
    for directory_name, repo_url in repo_dict.items():
        proceed_task(root_dir_name, directory_name, repo_url)


def execute_in_threads(root_dir_name: str, repo_dict: dict):
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(proceed_task, root_dir_name, directory_name, repo_url)
            for directory_name, repo_url in repo_dict.items()
        ]

    for future in futures:
        future.result()


def initializer(
    yaml_config_path: str = 'notgitmodules.yaml',
    download_in_threads: bool = True,
):
    """
    Initializes the download and clean-up process.

    :param yaml_config_path: The path to notgitmodules.yaml file
    :param download_in_threads: If you want to clone repos simultaneously or one at a time
    """
    yaml_content = read_yaml(yaml_config_path)

    for root_dir_name, repo_dict in yaml_content.items():
        ensure_dir_exists(root_dir_name)

        if download_in_threads:
            execute_in_threads(root_dir_name, repo_dict)
        else:
            execute_sequentially(root_dir_name, repo_dict)
