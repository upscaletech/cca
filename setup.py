#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['']


setup(name='Cca',
    version='1.0.3',
    description='A python wrapper for Carbon Chain Json-RPC API ',
    long_description=read('README.mkdn'),
    license="BSD",
    author='Saransh Sharma',
    author_email='saransh@theupscale.in',
    url='https://github.com/upscaletech/cca',
    keywords='carbon chain python blockchain adapter',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    )
