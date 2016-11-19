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


def write_config(configfile, content):
    """
    Write dict to a file in yaml format
    """
    with open(configfile, 'w+') as ymlfile:
        yaml.dump(
            content,
            ymlfile,
            default_flow_style=False,
        )
