import argparse
from .core import initializer


def cli():
    arg_parser = argparse.ArgumentParser(description="GitHub repositories installation with not_gitmodules.")

    # arguments
    arg_parser.add_argument(
        "-y", "--yaml-path",
        nargs="?",  # optional
        default="notgitmodules.yaml",
        help="Path to the custom YAML configuration file. By default it's notgitmodules.yaml."
    )

    # arg_parser.add_argument(
    #     "-d", "--dir_name",
    #     nargs="?",  # optional
    #     default="my_gitmodules",
    #     help="The name of the directory the modules will be saved in. By default it's my_gitmodules."
    # )

    # modes
    mode_group = arg_parser.add_mutually_exclusive_group()

    mode_group.add_argument(
        "-t", "--threaded",
        action="store_true",
        help="Enable threaded mode for parallel execution."
    )
    mode_group.add_argument(
        "-s", "--sequential",
        action="store_true",
        help="Enable sequential mode for sequential execution."
    )

    args, unknown = arg_parser.parse_known_args()

    download_in_threads = False if args.sequential else True

    initializer(
        yaml_config_path=args.yaml_path,
        # root_dir_name=args.dir_name,
        download_in_threads=download_in_threads
    )
