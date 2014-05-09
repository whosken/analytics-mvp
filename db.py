#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import json

import config

def get_host():
    return config.load()get('COUCH') or os.environ.get('CLOUDANT_URL') or 'http://localhost:5984'

def save(result):
    return requests.post(get_host()+'/tweets', data=json.dumps(result))
  
def load_latest(since_datetime):
    return requests.get(get_host()+'') # TODO: index
  
  