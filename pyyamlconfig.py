#!/bin/env python
# -*- coding: utf-8 -*-
"""Load configuration file in yaml format"""
import sys
import yaml

def load_config(configfile):
    """Return a dict with configuration from the supplied yaml file."""
    try:
        with open(configfile, 'r') as ymlfile:
            try:
                config = yaml.load(ymlfile)
            except yaml.parser.ParserError:
                print('Could not parse config file: %s' % configfile)
                sys.exit(1)
    except IOError:
        print('Could not open config file: %s' % configfile)
        sys.exit(1)
    return config
