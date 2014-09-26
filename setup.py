#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='pycloudsearch',
    version='0.1',
    description='Basic utilities to put stuff into cloudsearch',
    author='Edgar Roman',
    author_email='emroman@pbs.org',
    packages = find_packages(),
    include_package_data=True,
)
