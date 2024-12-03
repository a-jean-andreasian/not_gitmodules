import os
from .parts import delete_git_folder, ensure_dir_exists, extract_repo_name_from_url, clone_repo, read_yaml


def initializer(
    yaml_config_path: str = 'notgitmodules.yaml',
    root_dir_name="no_gitmodules"
):
    """
    :param yaml_config_path: The path to notgitmodules.yaml file
    :param root_dir_name: The name of directory where modules will be downloaded to.
    :return:
    """
    not_gitmodules = read_yaml(yaml_config_path)
    ensure_dir_exists(root_dir_name)

    for directory, repo_url in not_gitmodules.get("repos", {}).items():
        delete_git_folder(root_dir_name)

        clone_repo(root_dir_name, directory, repo_url)
        repo_name = extract_repo_name_from_url(repo_url)

        repo = os.path.join(root_dir_name, repo_name)
        delete_git_folder(repo)
