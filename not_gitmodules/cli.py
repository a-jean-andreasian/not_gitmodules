from .core import initializer


def cli():
    yaml_path = input('Enter the custom path to notgitmodules.yaml, or press any button to skip if it is in the root.')
    if not yaml_path.strip():
        initializer(yaml_config_path='notgitmodules.yaml')
    else:
        initializer(yaml_path.strip())
