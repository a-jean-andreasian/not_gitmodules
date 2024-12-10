import time
from not_gitmodules import initializer


def timer(func):
    def executor():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        return f'The execution of {func.__name__} took {end - start} seconds.'

    return executor


@timer
def test_sequentially():
    initializer(
        yaml_config_path='config.yaml',
        download_in_threads=False,
        root_dir_name='my_libs'
    )


@timer
def test_parallely():
    initializer(
        yaml_config_path='config.yaml',
        download_in_threads=True,
        root_dir_name='my_gitmodules'
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
