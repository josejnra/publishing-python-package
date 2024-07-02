# My Python Package

## What is needed?

```
my-first-package
├── LICENSE
├── pyproject.toml
├── README.md
├── setup.cfg
├── src
│   └── my_first_package
│       ├── __init__.py
│       └── list_dir.py
└── tests
```
- src/my_first_package/__init__.py - is required to import the directory as a package, and should be empty.
- src/my_first_package/list_dir.py - is an example of a module within the package that could contain the logic (functions, classes, constants, etc.) of your package.
- pyproject.toml - tells build tools (like pip and build) what is required to build your project. 
- setup.cfg - is the configuration file for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include.

## An "Old Way"

### Configuring metadata
There are two types of metadata: static and dynamic.

- Static metadata (`setup.cfg`): guaranteed to be the same every time. This is simpler, easier to read, and avoids many common errors, like encoding errors.
- Dynamic metadata (`setup.py`): possibly non-deterministic. Any items that are dynamic or determined at install-time, as well as extension modules or extensions to setuptools, need to go into setup.py.

Static metadata (setup.cfg) should be preferred. Dynamic metadata (setup.py) should be used only as an escape hatch when absolutely necessary. setup.py used to be required, but can be omitted with newer versions of setuptools and pip.

### Build
Make sure you have the latest version of PyPA’s build installed:
```python
python3 -m pip install --upgrade build
```

Run this command from the same directory where pyproject.toml is located:
```python
python3 -m build
```
The tar.gz file is a source archive whereas the .whl file is a built distribution. Newer pip versions preferentially install built distributions, but will fall back to source archives if needed.

### Testing Publishing
Publish the package to the TestPyPi repository to check if all works well.
Install twine:
```python
python3 -m pip install --upgrade twine
```
Twine is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes. It is a command-line program that passes program files and metadata to a web API. Developers use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.

Run Twine to upload all of the archives under dist:
```python
python3 -m twine upload --repository testpypi dist/*
```

### Installing and testing the package
Create a virtual environment then install the package:
```python
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps my-first-package-jose-nunes
```

Open a python terminal with the created venv:
```python
from my_first_package import list_dir
for i in list_dir.list_directories():
    print(i)
```

Note that the import package is my_first_package regardless of what name given in distribution package in setup.cfg or setup.py (in this case, my-first-package-jose-nunes).

## TODO: publish using poetry

## Referencies
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
