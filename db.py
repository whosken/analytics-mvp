#!/usr/bin/python
# -*- coding: utf-8 -*-

import couchdbkit
import os
import json

import config
  
def get_db():
    return (couchdbkit
            .Server(config.get('COUCH','CLOUDANT_URL','http://localhost:5984'))
            .get_or_create_db('tweets'))

def save(*results):
    return get_db().bulk_save(results)
  
def latest_sentiments(since_datetime):
    return get_db().view('realtime/sentiments', startkey=since_datetime)
