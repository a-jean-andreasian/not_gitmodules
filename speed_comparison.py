import os.path
import time
from not_gitmodules import initializer
import shutil


def timer_wrapper(root_dir_name):
    if os.path.exists(root_dir_name):
        shutil.rmtree(root_dir_name)

    def timer(func):
        nonlocal root_dir_name

        def executor():
            start = time.perf_counter()
            func(root_dir_name=root_dir_name)
            end = time.perf_counter()
            return f'The execution of {func.__name__} took {end - start} seconds.'

        return executor

    return timer


@timer_wrapper(root_dir_name='dev/my_libs')
def test_sequentially(root_dir_name):
    initializer(
        yaml_config_path='dev/config.yaml',
        download_in_threads=False,
        root_dir_name=root_dir_name
    )


@timer_wrapper(root_dir_name='dev/my_gitmodules')
def test_parallely(root_dir_name):
    initializer(
        yaml_config_path='dev/config.yaml',
        download_in_threads=True,
        root_dir_name=root_dir_name
    )


def compare():
    result1 = test_sequentially()
    time.sleep(2)
    result2 = test_parallely()

    print(70 * '=')
    print(result1)
    print(result2)


if __name__ == '__main__':
    compare()
