#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import os
import os.path
import yaml

def get(var, env_var=None, default=None):
    return get_val(var) or os.environ.get(env_var) or default

def get_val(var, _dict=None):
    val = _dict or load_yaml()
    for k in var.split('.'):
        if type(val) is dict:
            val = val.get(k)
    return val

default = 'config.yaml'
def load_yaml(path=None, filename=None):
    path = path or os.path.join(os.getcwd(), filename or default)
    logging.debug('Reading yaml from <{0}>'.format(path))
    with open(path) as file:
        return yaml.load(file.read())
