#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
import json

import config

def get_host():
    return config.load()get('COUCH') or os.environ.get('CLOUDANT_URL') or 'http://localhost:5984'

def save(*results):
    return requests.post(get_host()+'/tweets', data=json.dumps(results))
  
def latest_sentiments(since_datetime):
    response = requests.get(get_host()+'/_design/realtime/_view/sentiments',
                            params={'startkey':json.dumps(since_datetime)}).json()
    return response
    
  