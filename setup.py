#!/bin/env python
"""Setuptools file for pyyamlconfig"""
from setuptools import setup, find_packages

setup(name='pyyamlconfig',
      author='marhag87',
      url='https://github.com/marhag87/pyyamlconfig',
      version='0.1.0',
      packages=find_packages(),
      license='WTFPL',
      description='Load configuration file in yaml format',
      long_description='Load configuration file in yaml formaẗ́',
      requirements=['pyyaml', 'sys'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: WTFPL',
          'Programming Language :: Python :: 3',
      ],
     )
