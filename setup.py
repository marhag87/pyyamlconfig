#!/bin/env python
"""
Setuptools file for pyyamlconfig
"""
from setuptools import (
    setup,
    find_packages,
)

setup(
    name='pyyamlconfig',
    author='marhag87',
    author_email='marhag87@gmail.com',
    url='https://github.com/marhag87/pyyamlconfig',
    version='0.2.3',
    packages=find_packages(),
    license='WTFPL',
    description='Load configuration file in yaml format',
    long_description='Load configuration file in yaml formaẗ́',
    install_requires=['PyYAML'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
