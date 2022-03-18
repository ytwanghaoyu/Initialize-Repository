# -*- coding: utf-8 -*-
# Copyright 2022 The my repo Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""Welcome to the Pymy repo setup.py.

We strongly recommand you install via pypi source instead.
"""

import io
import os
import sys
import typing
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Package meta-data.
NAME = "my-repo"
DESCRIPTION = "Pymy repo."
URL = "https://git.nevint.com/algo-dev-platform/my_repo"
EMAIL = "adp@nio.com"
AUTHOR = "Algorithm Development Platform Team"
REQUIRES_PYTHON = ">=3.8.0"
REQ_DIR = "./requirements"

HERE = os.path.abspath(os.path.dirname(__file__))


def load_requirements(file_path):
    """Parse the package dependencies listed in a requirements file."""
    valid_lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()
            if len(line) > 0 and line[0].isalpha():
                valid_lines.append(line)
    return valid_lines


def get_long_description():
    """Import the README and use it as the long-description.

    Note: this will only work if 'README.md' is present in your MANIFEST.in file!
    """
    try:
        with io.open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
            long_description = "\n" + f.read()
    except FileNotFoundError:
        long_description = DESCRIPTION
    return long_description


# What packages are required for this module to be executed?
REQUIRED = load_requirements(os.path.join(REQ_DIR, "./install.txt"))

# What packages are optional?
EXTRAS = {
    "develop": load_requirements(os.path.join(REQ_DIR, "./develop.txt")),
    "release": load_requirements(os.path.join(REQ_DIR, "./release.txt")),
    "test": load_requirements(os.path.join(REQ_DIR, "./test.txt")),
    "fancy feature": [],
}

# What the long description is?
LONG_DESCRIPTION = get_long_description()


def load_version():
    """Load the package's __version__.py module as a dictionary.

    Note: this will only work if '__version__.py' exist!
    """
    import my_repo

    return my_repo.__version__


# Where the magic happens:
setup(
    name=NAME,
    use_scm_version=True,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(
        exclude=["dist.*", "dist", "tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
