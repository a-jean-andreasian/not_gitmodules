from setuptools import setup, find_packages

setup(
    name='not_gitmodules',
    version='0.1.3.1',
    packages=find_packages(),
    license='Custom License',
    entry_points={
        'console_scripts': [
            'not_gitmodules=not_gitmodules.cli:cli',
        ],
    },
    install_requires=[
        'pyyaml',
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Armen-Jean Andreasian',
    author_email='armen_andreasian@proton.me',
    description='A library for managing git repositories in a directory.',
    url='https://github.com/Armen-Jean-Andreasian/not_gitmodules',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
    ],
)
