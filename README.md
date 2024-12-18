
<div style="text-align: center;">
  <img src=".github/pic1.png" />
</div>

---

# What's  `not_gitmodules`?

Watch the intro:

[![](https://markdown-videos-api.jorgenkh.no/youtube/QkFxP_6NA84)](https://youtu.be/QkFxP_6NA84)

Long story short: `not_gitmodules` is a lightweight, production-ready Python utility designed to simplify managing external modules in
your project.

---

# Why `not_gitmodules`?

1. Simplicity: Minimalistic design—no unnecessary complexities.
2. Production-Ready: Explicitly licensed for production use.
3. Dependency-Free: Uses only Python's built-in tools.
4. OS-Agnostic: Works seamlessly on Linux, MacOS and any other platforms where Python is available by default.

--- 

## Important note

1. not_gitmodules just like Gitmodules doesn't `automatically install the dependencies`/`do not include the dependencies to your project dependency file (such as requirements.txt for Python or package.json for JavaScript)` of the submodule.
2. not_gitmodules doesn't `download the submodules mentioned in the not_gimodules.yaml file of the submodule`.
- Reason: it's practically inefficient, may lead to bugs and bottlenecks, and better to maintain manually.

How to handle?
1. Move the containing of the dependency file to your project's dependency file and rerun the dependency installer.

2.1. Important note. `not_gitmodules` keeps the view of keeping the project structure clean. All submodules amoung one project/micro-service need to go to one folder. It's recommended to use dependency injection in case of having nested not_gitmodules.

2.2. Move submodules to your `not_gimodules.yaml` file and rerun install accordingly.

## Installation and Usage

### Installation

Choose one of the following methods to install `not_gitmodules`:

#### 1. Clone the repository:

```bash  
git clone https://github.com/Armen-Jean-Andreasian/not_gitmodules.git
```  

#### 2. Install via pip:

```bash  
pip install not-gitmodules
```  

---

# Preparation and Usage Options

## 1. Preparation (IMPORTANT)

Create a `notgitmodules.yaml` file in your project's root directory.

```yaml
# directory_name: url (ssh or https)  

# Example: 
utils:
  file_manager: https://github.com/not-gitmodules/notgitmodules-file-manager-py
  file_encryptor: https://github.com/not-gitmodules/notgitmodules-file-encryptor-py

services:
  forsaken_mail: https://github.com/malaohu/forsaken-mail
  sim_mail: https://github.com/Webador/SlmMail
```  

## 2. Usage Options

You can use `not_gitmodules` in two ways:

1. **As a part of your project's code.**  
   Just clone/download this repository and include it to your project.
    - **Pros:** No additional dependencies or overhead.
    - **Cons:** No CLI usage; increases the project's file size.


2. **As a Python Package (Recommended).**  
   Install using **pip**

- **Pros:** This method allows you to leverage CLI commands for better flexibility, ease with Docker, keeps the project
  lightweight
    - **Cons:** Additional dependency

**Not recommended** option: clone/download this repository and run `pip install .`

---

# Usage

## A. As Part of Your Project's Code

### Command:

```bash  
git clone https://github.com/Armen-Jean-Andreasian/not_gitmodules.git
```  

### Implementation:

- If `notgitmodules.yaml` is located in the project root:

```python
from not_gitmodules import initializer

initializer()  
```  

- If `notgitmodules.yaml` is located somewhere else. _Or has a different name._

```python
from not_gitmodules import initializer

initializer('custom/path/to/config.yaml')  # Specify a custom path  
```  

  
---  

## B. As a Python Package (Recommended)

This method allows you to leverage CLI commands for better flexibility.

### 1. Install the package

```  
pip install not_gitmodules 
```  

---  

### 2. Add it to `requirements.txt`

As this package is not used in code itself, it's easy to forget to add. So better to add in advance.

#### Run:

```bash  
pip show not_gitmodules
```  

**Check the `Version` and include it to `requirements.txt` with `~=` assignment:**

- Example:
    ```text
    not_gitmodules~=0.0
    ```

---  

### 3. Install the modules:

| Flag (all of them are optional) | Description                                                                                                                                                                                                                                      | Example                                                                                                                                |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| `-y`, `--yaml-path`             | Specify a custom path for the `notgitmodules.yaml` configuration file. <br>By default, it looks for `notgitmodules.yaml` in the current working directory. Naming it `notgitmodules` is a matter of best practices; you can name it as you want. | • `not_gitmodules -y /path/to/custom_notgitmodules.yaml`: Uses a custom YAML file located at `/path/to/custom_notgitmodules.yaml`      |
| `-t`, `--threaded`              | Enable threaded execution, where repositories are cloned in parallel (using threads). This flag is mutually exclusive with `-s`. <br> This is the default behavior if neither `-t` nor `-s` is specified.                                        | • `not_gitmodules -t`: Clones repositories in parallel using threads <br> • `not_gitmodules --threaded`: Same as `-t`, using long form |
| `-s`, `--sequential`            | Enable sequential execution, where repositories are cloned one by one in the order they appear in the YAML file. This flag is mutually exclusive with `-t`.                                                                                      | • `not_gitmodules -s`: Clones repositories one by one in order <br> • `not_gitmodules --sequential`: Same as `-s`, using long form     |

### More command examples:

- ### Default command:

This will look for `notgitmodules.yaml` in the project root and create a directory named `my_gitmodules` in the root to
download the modules into, in parallel mode using threads.

```bash  
not_gitmodules install
```

- ### Command pattern:

```bash  
not_gitmodules install --yaml-path </path/to/notgitmodules.yaml>  --threaded
```  

or

```bash  
not_gitmodules install -y </path/to/notgitmodules.yaml>  -t
```

---

## Comparison

Usually with undefined amount of workers in `ThereadPool` in parallel mode take more than **52%** less time than in
parallel mode.


---  

### 4. Dockerizing

Double-check that you:

1. Created a `notgitmodules.yaml`
2. Included `not_gitmodules` version to `requirements.txt`

Then:

3. Create your `Dockerfile`. Example:

```dockerfile  
FROM python:3.10-slim  

# Install git for not_gitmodules
RUN apt-get update && apt-get install -y git  
  
WORKDIR /app  
  
COPY . .  
  
RUN pip install --no-cache-dir -r requirements.txt   

# copy the notgitmodules.yaml file (default). Modify accordingly.
COPY notgitmodules.yaml .

# install modules using not_gitmodules
RUN not_gitmodules install -y notgitmodules.yaml -t
  
CMD ["python", "main.py"]
```

---

## Possible Issues with Private Repositories

If cloning fails but you have access to the repository, provide the HTTPS repo URL instead of SSH  
in `notgitmodules.yaml`.

---

## Worth to mention

- `not_gitmodules` doesn't require for you to keep the folders with modules. You can safely .gitignore/delete them.
- Do not use matching names for the repositories in `notgitmodules.yaml` file. In that case only the first repository
  will be downloaded and the second one - skipped.

---

## License

This project is licensed under a **Custom License**. See the [LICENSE](./LICENSE) file for full details.

Key points:

- You may use this project for commercial or personal purposes.

---

## Author

Armen-Jean Andreasian, 2024

---

<div style="text-align: center;">
  <img src=".github/pic2.png" />
</div>
