# <img src="https://raw.githubusercontent.com/a-jean-andreasian/not_gitmodules/refs/heads/master/.github/logo_v2.png" alt="Not Gitmodules!" height="30" /> Not Gitmodules

---


## Introduction

- Not Gitmodules is a **lightweight**, **production-friendly** and **open-source** Python utility
  designed to simplify managing external modules in
  your project.
- It's a replacement for Git Submodule which is: up to **10x faster**, **safer**, **simpler**, **cleaner** and the most
  importantly - **without headaches**.

---

## Effortlessness

Everything you need to do is:

1. Install Not Gitmodules. Clone this repo from GitHub or install from PyPi
2. Create a simple YAML file.

Not Gitmodules will handle the rest for you.

---

## Why Not Gitmodules?

1. **Simplicity**: Minimalistic design and no unnecessary complexities.
2. **Production-Ready**: Explicitly licensed for production use.
3. **Dependency-Free**: Uses only Python's built-in tools.
4. **OS-Agnostic**: Works seamlessly on Linux, MacOS and any other platforms where Python is available by default.

---

## Still have questions?

Watch the introduction video on YouTube, where Snoop Dogg will explain everything!

[![](https://markdown-videos-api.jorgenkh.no/youtube/QkFxP_6NA84)](https://youtu.be/QkFxP_6NA84)

---

## Usage



### Part 1: Installation

Choose the most convenient way to install Not Gitmodules:

1. **Clone** (or download) this repository and include it to your project and use **as a part of your project's code:**

   ```
   git clone git@github.com:Armen-Jean-Andreasian/not_gitmodules.git
   ```


2. **Install via a package manager** and use **as a Python package** _(example with pip)_:

    ![PyPI](https://img.shields.io/pypi/v/not-gitmodules)
    ```bash  
    pip install not-gitmodules
    ```  
    - And, yeah, don't forget to add it to `requirements.txt` in advance, if you don't use Poetry.

---

### Part 2: Preparation

1. Create a YAML file in your project's root directory.

- Tip: Naming it `notgitmodules.yaml` lets you use it without explicitly specifying it in the command.

2. Define the submodules following the pattern:

```yaml
folder_to_save: # Destination folder for this group of modules
  module1: module1.url # directory_name: url (ssh or https)
  module2: module2.url

another_folder:
  module3: module3.url
```

Example:

```yaml
# directory_name: url (ssh or https)  
utils:
  file_manager: https://github.com/not-gitmodules/notgitmodules-file-manager-py
  file_encryptor: https://github.com/not-gitmodules/notgitmodules-file-encryptor-py

services:
  forsaken_mail: https://github.com/malaohu/forsaken-mail
  sim_mail: https://github.com/Webador/SlmMail
```  

The example above will download and create this structure:

```
utils/
    file_manager/
        ... (containing of the repo)
    file_encryptor/
        ...

services:
    forsaken_mail/
        ...
    sim_mail/
        ...
```

---

### Part 3: Installation

| Flag (all of them are optional)              | Description                                                                                                                                                                                                            | Example                                                                                                                                |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `-y`, `--yaml-path`                          | Specify a custom path for the YAML file. <br>By default, it looks for `notgitmodules.yaml` in the current working directory. <br>Naming it `notgitmodules` is a matter of best practices; you can name it as you want. | • `not_gitmodules -y /path/to/custom_notgitmodules.yaml`: Uses a custom YAML file located at `/path/to/custom_notgitmodules.yaml`      |
| `-t`, `--threaded` _**(default behaviour)**_ | Enable threaded execution, where repositories are cloned in parallel (using threads). <br>This flag is mutually exclusive with `-s`. <br> This is the default behavior if neither `-t` nor `-s` is specified.          | • `not_gitmodules -t`: Clones repositories in parallel using threads <br> • `not_gitmodules --threaded`: Same as `-t`, using long form |
| `-s`, `--sequential`                         | Enable sequential execution, where repositories are cloned one by one in the order they appear in the YAML file. This flag is mutually exclusive with `-t`.                                                            | • `not_gitmodules -s`: Clones repositories one by one in order <br> • `not_gitmodules --sequential`: Same as `-s`, using long form     |

#### More command examples:

- ### Default command:

This will look for `notgitmodules.yaml` in the project root and create a directory named `my_gitmodules` in the root to
download the modules into, in parallel mode using threads.

```bash  
not_gitmodules install
```

- ### Command pattern:

```bash  
not_gitmodules install --yaml-path </path/to/notgitmodules.yaml>  --<execution_type> 
```  

or

```bash  
not_gitmodules install -y </path/to/notgitmodules.yaml>  --sequential
```


> Note: Usually with undefined amount of workers in `ThereadPool` in parallel mode take more than **52%** less time than in
parallel mode.

---

### Part 4. Dockerizing


```dockerfile  
FROM python:3.10-slim  

# Install git for not_gitmodules
RUN apt-get update && apt-get install -y git  

RUN pip install --no-cache-dir -r requirements.txt   

# copy the notgitmodules.yaml file (default). Modify accordingly.
COPY notgitmodules.yaml .

# install modules using not_gitmodules.
RUN not_gitmodules install -y notgitmodules.yaml -t

WORKDIR /app  
  
COPY . .

CMD ["python", "main.py"]
```

---

## Good to Know

1. Not Gitmodules **doesn't require to keep the folders** with modules. You can safely .gitignore or delete them.
2. **Do not use matching names** for the repositories in `notgitmodules.yaml` file. In that case only the first repository
  will be downloaded and the second one will be skipped.
3. Not Gitmodules **needs** `Git` and `PyYAML` for functioning.
4. Not Gitmodules, just like Gitmodules, **doesn't automatically install the dependencies of submodules** _(such as requirements.txt for Python or package.json for JavaScript)_.
5. Not Gitmodules **doesn't download the sub-dependency submodules** (if they are not defined properly for Git).
   - Reason: it's practically inefficient, may lead to bugs and bottlenecks, and better to maintain manually.
   - Solution: Include the sub-dependency submodule to YAML file manually.
6. Not Gitmodules keeps the view of keeping the project structure clean. All submodules among one
   project/microservice need to go to one folder. It's recommended to use dependency injection in case of having nested `not_gitmodules`.
7. **Possible bottleneck** with private repositories. 
    -  If cloning fails, but you have access to the repository, provide the HTTPS repo URL instead of SSH url in YAML file.


---

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/a-jean-andreasian/not_gitmodules/refs/heads/master/.github/pic1.png" width="300" height="300">
</div>

---

## ![License](https://img.shields.io/badge/license-Custom-blue)

This project is licensed under a **Custom License**. See the [LICENSE](./LICENSE) file for full details.

Key points:

- You may use this project for commercial or personal purposes.

---

## Author

Armen-Jean Andreasian, 2024

---

<div style="text-align: center;">
  <img src="https://raw.githubusercontent.com/a-jean-andreasian/not_gitmodules/refs/heads/master/.github/pic2.png" />
</div>

