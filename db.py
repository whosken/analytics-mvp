#!/usr/bin/python
# -*- coding: utf-8 -*-

import couchdbkit
import couchdbkit.exceptions
import collections

import config
  
def get_db():
    return (couchdbkit
            .Server(config.get('COUCH','CLOUDANT_URL','http://localhost:5984'))
            .get_or_create_db('tweets'))

def save(*results):
    try:
        return get_db().bulk_save(results)
    except couchdbkit.exceptions.BulkSaveError as error:
        print error
  
def latest_sentiments(since_datetime=None):
    counter = collections.Counter()
    for r in get_db().view('realtime/sentiments', startkey=since_datetime, group=True):
        counter.update(r['value'])
    counter += collections.Counter()
    return dict(counter)