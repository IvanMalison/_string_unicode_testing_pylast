#!/usr/bin/env python
import os

from setuptools import setup, find_packages


setup(
    name="dumb",
    version="1.0.0",
    author="Amr Hassan <amr.hassan@gmail.com>",
    keywords=["Last.fm", "music", "scrobble", "scrobbling"],
    packages=find_packages(exclude=('tests*')),
    license="Apache2"
)

# End of file
