# ⚠️ NOTICE: PROJECT NO LONGER MAINTAINED

This project is no longer maintained as our focus has shifted. Although flagged as End of Life (EOL) since December 2022, Second Brain Tools remains available for reference and legacy purposes.

# Second Brain Tools

[![GitHub Actions Build Status](https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/pylint.yml/badge.svg)](https://github.com/rohanbatrain/Second-Brain-Tools/actions/)
[![GitHub Actions Build Status](https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/build.yml/badge.svg)](https://github.com/rohanbatrain/Second-Brain-Tools/actions/)
[![GitHub Actions Build Status](https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/mkdocs.yml/badge.svg)](https://github.com/rohanbatrain/Second-Brain-Tools/actions/)
[![Coverage Status](https://codecov.io/gh/rohanbatrain/Second-Brain-Tools/branch/main/graphs/badge.svg?branch=main)](https://codecov.io/github/rohanbatrain/Second-Brain-Tools)
[![PyPI Package Latest Release](https://img.shields.io/pypi/v/second-brain-tools.svg)](https://pypi.org/project/second-brain-tools)
[![PyPI Wheel](https://img.shields.io/pypi/wheel/second-brain-tools.svg)](https://pypi.org/project/second-brain-tools)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/second-brain-tools.svg)](https://pypi.org/project/second-brain-tools)
[![Supported Implementations](https://img.shields.io/pypi/implementation/second-brain-tools.svg)](https://pypi.org/project/second-brain-tools)

_A comprehensive toolset designed for rapid note creation using the Second Brain Vault._

---

## Overview

Second Brain Tools is a robust suite of utilities designed to streamline the process of creating, organizing, and managing notes via the Second Brain Vault. Built with Python 3 and Git, this project was originally maintained under the Apache 2.0 License.

---

## Prerequisites

Before installation, ensure you have:

- **Python 3** and **pip** installed.
- **Git** installed on your system.

---

## Installation

To install the latest stable version from PyPI, run:

```bash
pip install second-brain-tools
```

For the in-development version directly from GitHub:

```bash
pip install https://github.com/rohanbatrain/Second-Brain-Tools/archive/main.zip
```

---

## Usage

The toolset offers a command-line interface (CLI) to interact with the Second Brain Vault. To get started, run the following command from your Python environment:

```python
from second_brain_tools import cli
cli.main()
```

Alternatively, execute the CLI directly from your terminal.

---

## Documentation

Comprehensive documentation is available on the [Second Brain Tools Documentation Site](https://rohanbatrain.github.io/second-brain-tools-2022/). Note that this documentation represents a partial set of guidelines, with no planned hotfixes or further updates.

---

## Development

To run the full suite of tests, use [tox](https://tox.readthedocs.io/):

```bash
tox
```

To combine coverage data across all tox environments:

- **On Windows:**

  ```bash
  set PYTEST_ADDOPTS=--cov-append
  tox
  ```

- **On other systems:**

  ```bash
  PYTEST_ADDOPTS=--cov-append tox
  ```

---

## Changelog

### 2024
- Minor upgrades implemented to support integration into my Semester-2 college assignment.

### 2023

#### July
- Partial documentation was published [here](https://rohanbatrain.github.io/second-brain-tools-2022/). No further documentation updates or hotfixes are planned.

#### June
- Released a hotfix for the PyPI package (version 0.0.4) addressing issues caused by changes in the GitHub repository naming scheme.
- Discontinued support for PyPy 3.7.
- Ongoing work on documentation improvements.

### End of Life (EOL)
- The project has been flagged as EOL since December 2022. While the repository remains available for reference, no further updates or support will be provided.

---

## License

This project is licensed under the [Apache Software License 2.0](LICENSE).
