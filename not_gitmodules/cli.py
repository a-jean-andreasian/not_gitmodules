import argparse
from .core import initializer


def cli():
    arg_parser = argparse.ArgumentParser(description="GitHub repositories installation with not_gitmodules.")

    arg_parser.add_argument(
        "-y", "--yaml-path",
        nargs="?",  # optional
        default="notgitmodules.yaml",
        help="Path to the custom YAML configuration file. By default it's notgitmodules.yaml."
    )

    arg_parser.add_argument(
        "-d", "--dir_name",
        nargs="?",  # optional
        default="my_gitmodules",
        help="The name of the directory the modules will be saved in. By default it's my_gitmodules."
    )

    args, unknown = arg_parser.parse_known_args()

    initializer(yaml_config_path=args.yaml_path, root_dir_name=args.dir_name)
