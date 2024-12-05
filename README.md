# Not Gitmodules

---

## Why `not_gitmodules`?

1. `not_gitmodules` demonstrate how simple and elegant `gitmodules` should be to those developers who enjoy their lives.
   Add and remove modules without caring about irrelevant stuff. No *
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
Here's the updated `README.md` snippet with the changes you requested:

---

## Usage

1. **IMPORTANT:** Create a `notgitmodules.yaml` file in your project's root directory.

```yaml
# directory_name: url (ssh or https)
# example:
file_reader: https://github.com/Free-Apps-for-All/file_manager_git_module
```

2. Let `not_gitmodules` do the job.

> ### Example with Code:
>
> Pass the path to the `initializer` function:
> ```python
> from not_gitmodules import initializer
> 
> initializer('custom/path/to/notgitmodules.yaml')
> ```
> or
> ```python
> from not_gitmodules import initializer
> 
> initializer()  # if notgitmodules.yaml exists in the project root
> ```

### Example with CLI:

#### 1. Install the library locally if you cloned the repo (**optional**) :

  ```bash
  pip install .
  ```

---

#### 2. Install the modules directly from the terminal:

>#### Flags
>
>| Flag                | Description                                                             |
>|---------------------|-------------------------------------------------------------------------|
>| `-d`, `--dir_name`  | Specify a directory name where the modules will be saved (optional).    |
>| `-y`, `--yaml-path` | Specify a custom location for the `notgitmodules.yaml` file (optional). |

### Default command:

```bash
not_gitmodules install
```

### Command pattern:

```bash
not_gitmodules install --yaml-path </path/to/notgitmodules.yaml>  --dir_name <directory_name>
```

or

```bash
not_gitmodules install -y </path/to/notgitmodules.yaml>  -d <directory_name>
```


### Do not forget to add `not_gitmodules` to `requirements.txt`

Run 

```bash
pip show not_gitmodules
```

Check the `Version` and include it to `requirements.txt`

Example:
```text
not_gitmodules~=0.2
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
