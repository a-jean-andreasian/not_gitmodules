import os
from .parts import delete_git_folder, ensure_dir_exists, clone_repo, read_yaml, clean_github_leftovers


def initializer(
    yaml_config_path: str = 'notgitmodules.yaml',
    root_dir_name="my_gitmodules"
):
    # Read yaml
    # Ensure root_dir exists
    # Clone the repo to root dir
    # Clean-up

    """
    :param yaml_config_path: The path to notgitmodules.yaml file
    :param root_dir_name: The name of directory where modules will be downloaded to.
    :return:
    """
    not_gitmodules = read_yaml(yaml_config_path)
    ensure_dir_exists(root_dir_name)

    for directory, repo_url in not_gitmodules.items():
        clone_repo(root_dir_name, directory, repo_url)

        module_path = os.path.join(root_dir_name, directory)
        delete_git_folder(module_path)
        clean_github_leftovers(module_path)
