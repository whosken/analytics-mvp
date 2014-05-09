#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import json

import config

def get_host():
    return os.environ.get('CLOUDANT_URL') or config.load()['COUCH']

def save(result, id_=None):
    if id_: result['_id'] = id_
    if 'datetime' in result: result['datetime'] = str(result['datetime'])
    return requests.post(get_host() + '/', data=json.dumps(result))
  
def load_summary():
    pass
  
def load_latest():
    pass
  
  