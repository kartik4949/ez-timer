# Copyright 2022 Luke Wood
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup script."""

from setuptools import find_packages
from setuptools import setup

setup(
    name="ez-timer",
    description="The simplest way to time a block of code.",
    url="https://github.com/lukewood/ez-timer",
    author="Luke Wood",
    author_email="lukewoodcs@gmail.com",
    license="Apache License 2.0",
    install_requires=[],
    extras_require={
        "tests": ["flake8", "isort", "black", "pytest"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Topic :: Software Development",
    ],
    packages=find_packages(exclude=("*_test.py",)),
)