# Not Gitmodules

---

## Why this?

1. This is how simple `gitmodules` should be. Add and remove modules without caring about irrelevant stuff. No *
   *shitshow**, just simplicity.
2. Production-use friendly. This is documented in the license.
3. No third-party libraries are required; only built-in tools are used.
4. OS-agnostic. Written in Python, meaning it can be used in any type of project, especially those running on Linux.

---

## Installation

- Clone the repository using Git.
- Install via pip:

  ```bash
  pip install not-gitmodules
  ```

---

## Usage

**IMPORTANT:** Create a `notgitmodules.yaml` file in your project's root directory.

1. **Example with Code**:

   Create a `notgitmodules.yaml` file:

   ```yaml
   repos:
     # directory: url (ssh or https)

     # Example
     file_reader: https://github.com/Free-Apps-for-All/file_manager_git_module
   ```

   Then pass the path to the `initializer` function:

   ```python
   from not_gitmodules import initializer

   initializer('/path/to/notgitmodules.yaml')
   ```

2. **Example with CLI**:

   Install the library locally if you cloned the repo:

   ```bash
   pip install .
   ```

   Once installed, you can delete the local repo from your system (the library is now saved in the virtual environment
   or globally).

   Run `not_gitmodules` directly from the terminal:

   ```bash
   not_gitmodules
   ```

---

## Possible Issues with Private Repositories

If cloning fails but you have access to the repository, provide the HTTPS repo URL instead of SSH
in `notgitmodules.yaml`.

---

## That's it!

No more wasted time with `.git`, metadata, and other bloat that offer no real tradeoff.

---

## Recommended Modifications

After cloning the repository, delete unnecessary files if you're customizing or using the project for specific purposes:

- `not_gitmodules\.gitignore`
- `not_gitmodules\LICENSE`
- `not_gitmodules\README.md`
- `not_gitmodules\setup.py` (if you're not using it as a CLI tool or environment package)
- `not_gitmodules/cli.py` (if you're not using the installer in a CLI context)

---

## Author

Armen-Jean Andreasian, 2024

---

## License

This project is licensed under a **Custom License**. See the [LICENSE](./LICENSE) file for full details.

Key points:

- You may use this project for commercial or personal purposes.
- You may not claim ownership of this project or its code.

---