#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import os.path
import yaml

def load(path=None, overwrite=None):
    config = load_yaml(path)
    overwrite = overwrite or os.environ.get('CONFIG')
    if overwrite:
        config.update(load_yaml(filename=overwrite))
    return config

default = 'config.yaml'
def load_yaml(path=None, filename=None):
    path = path or os.path.join(os.getcwd(), filename or default)
    logging.debug('Reading yaml from <{0}>'.format(path))
    with open(path) as file:
        return yaml.load(file.read())
