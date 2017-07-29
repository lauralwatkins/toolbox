#!/usr/bin/env python

from setuptools import setup

setup(
    name="toolbox",
    version="0.0",
    description="A random collection of useful Python functions.",
    author="Laura L Watkins",
    author_email="lauralwatkins@gmail.com",
    url="https://github.com/lauralwatkins/toolbox",
    package_dir = {
        "toolbox": "toolbox",
    },
    packages=["toolbox"],
)
