import os
from .parts import delete_git_folder, ensure_dir_exists, clone_repo, read_yaml, clean_github_leftovers
from concurrent.futures import ThreadPoolExecutor


def execute_sequentially(root_dir_name: str, yaml_content: dict):
    for directory, repo_url in yaml_content.items():
        clone_repo(root_dir_name=root_dir_name, directory_name=directory, url=repo_url)

        module_path = os.path.join(root_dir_name, directory)
        delete_git_folder(module_path)
        clean_github_leftovers(module_path)


def execute_in_threads(root_dir_name: str, yaml_content: dict):
    def proceed_task(root_dir_name, directory, repo_url):
        """Packed-up collection of actions, to run in a separate thread."""
        clone_repo(root_dir_name=root_dir_name, directory_name=directory, url=repo_url)

        module_path = os.path.join(root_dir_name, directory)
        delete_git_folder(module_path)
        clean_github_leftovers(module_path)

    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(proceed_task, root_dir_name, directory, repo_url)
            for directory, repo_url in yaml_content.items()
        ]

    for future in futures:
        future.result()


def initializer(
    yaml_config_path: str = 'notgitmodules.yaml',
    root_dir_name="my_gitmodules",
    download_in_threads: bool = True,
):
    # Read yaml
    # Ensure root_dir exists
    # Clone the repo to root dir
    # Clean-up

    """
    :param yaml_config_path: The path to notgitmodules.yaml file
    :param root_dir_name: The name of directory where modules will be downloaded to.
    :param download_in_threads: If you want to clone repos simultaneously or one at a time
    # :param max_threads: Maximum amount of allowed threads
    :return:
    """
    yaml_content = read_yaml(yaml_config_path)
    ensure_dir_exists(root_dir_name)

    if download_in_threads:
        execute_in_threads(root_dir_name, yaml_content)
    else:
        execute_sequentially(root_dir_name, yaml_content)
