========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions| |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |travis| image:: https://api.travis-ci.com/rohanbatrain/Second-Brain-Tools.svg?branch=main
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/rohanbatrain/Second-Brain-Tools

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/rohanbatrain/Second-Brain-Tools?branch=main&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/rohanbatrain/Second-Brain-Tools

.. |github-actions| image:: https://github.com/rohanbatrain/Second-Brain-Tools/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/actions

.. |requires| image:: https://requires.io/github/rohanbatrain/Second-Brain-Tools/requirements.svg?branch=main
    :alt: Requirements Status
    :target: https://requires.io/github/rohanbatrain/Second-Brain-Tools/requirements/?branch=main

.. |codecov| image:: https://codecov.io/gh/rohanbatrain/Second-Brain-Tools/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/rohanbatrain/Second-Brain-Tools

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

.. |commits-since| image:: https://img.shields.io/github/commits-since/rohanbatrain/Second-Brain-Tools/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/rohanbatrain/Second-Brain-Tools/compare/v0.0.1...main



.. end-badges

This is a module set for all the python utils that are being used on Second brain project and its subsequent Children.

* Free software: Apache Software License 2.0

Installation
============

::

    pip install second-brain-tools

You can also install the in-development version with::

    pip install https://github.com/rohanbatrain/Second-Brain-Tools/archive/main.zip


Documentation
=============


To use the project:

.. code-block:: python

    import second_brain_tools
    second_brain_tools.longest()


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
