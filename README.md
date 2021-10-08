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

## Configuring metadata
There are two types of metadata: static and dynamic.

- Static metadata (`setup.cfg`): guaranteed to be the same every time. This is simpler, easier to read, and avoids many common errors, like encoding errors.
- Dynamic metadata (`setup.py`): possibly non-deterministic. Any items that are dynamic or determined at install-time, as well as extension modules or extensions to setuptools, need to go into setup.py.

Static metadata (setup.cfg) should be preferred. Dynamic metadata (setup.py) should be used only as an escape hatch when absolutely necessary. setup.py used to be required, but can be omitted with newer versions of setuptools and pip.

## Build
Make sure you have the latest version of PyPA’s build installed:
```python
python3 -m pip install --upgrade build
```

Run this command from the same directory where pyproject.toml is located:
```python
python3 -m build
```
The tar.gz file is a source archive whereas the .whl file is a built distribution. Newer pip versions preferentially install built distributions, but will fall back to source archives if needed.

## Testing
Publish the package to the TestPyPi repository to check if all works well.


## Referencies
- [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/)
