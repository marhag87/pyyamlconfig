#!/bin/env python
# -*- coding: utf-8 -*-
"""
Load configuration file in yaml format
"""
import yaml


class PyYAMLConfigError(Exception):
    """
    Generic PyYAMLConfig Error
    """
    pass


def load_config(configfile):
    """
    Return a dict with configuration from the supplied yaml file
    """
    try:
        with open(configfile, 'r') as ymlfile:
            try:
                config = yaml.load(ymlfile)
                return config
            except yaml.parser.ParserError:
                raise PyYAMLConfigError(
                    'Could not parse config file: {}'.format(configfile),
                )
    except IOError:
        raise PyYAMLConfigError(
            'Could not open config file: {}'.format(configfile),
        )
