========
EOL
========

The project has been flagged as EOL (End of Life) on December 2022. Moving forward to more simplistic approach for better automation and other changes. You can still use the structure but please dont expect more updates or support.


Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |pylint| |build| |mkdocs| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |pylint| image:: https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/pylint.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/actions/
    
.. |build| image:: https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/build.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/actions/

.. |mkdocs| image:: https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/mkdocs.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/actions/

.. |codecov| image:: https://codecov.io/gh/rohanbatrain/Second-Brain-Tools/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/rohanbatrain/Second-Brain-Tools

.. |requires| image:: https://requires.io/github/rohanbatrain/Second-Brain-Tools/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/rohanbatrain/Second-Brain-Tools/requirements/?branch=main

.. |version| image:: https://img.shields.io/pypi/v/second-brain-tools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/second-brain-tools

.. |wheel| image:: https://img.shields.io/pypi/wheel/second-brain-tools.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/second-brain-tools

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/second-brain-tools.svg
    :alt: Supported versions
    :target: https://pypi.org/project/second-brain-tools

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/second-brain-tools.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/second-brain-tools

.. |commits-since| image:: https://img.shields.io/github/commits-since/rohanbatrain/Second-Brain-Tools/v0.0.3.svg
    :alt: Commits since latest release
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/compare/v0.0.3...main



.. end-badges

This project is a toolset for Second Brain, This would help us to quickly and more efficiently create notes using
Second Brain Vault.

* Free software: Apache Software License 2.0

Installation
============

::

    pip3 install second-brain-tools

You can also install the in-development version with::

    pip install https://github.com/rohanbatrain/Second-Brain-Tools/archive/main.zip


Documentation
=============

Please note the developement is paused for 3 months due to 12th -> (CBSE BOARDS 2023) 

To use the project:

.. code-block:: python

    from second_brain_tools import cli  
    cli.main()
    
Or from your terminal

.. code-block:: bash

    second-brain-tools --help
    
Currently no time for writing docs, join me on the discussion on obsidian forums.

https://forum.obsidian.md/t/second-brain-vault-template-cli/50758




Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
