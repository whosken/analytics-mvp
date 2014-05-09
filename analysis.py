#!/usr/bin/python
# -*- coding: utf-8 -*-

import textblob
import datetime

import db
import queue

to_blob = textblob.Blobber()

def work(tweet):
    return db.save(analyze(tweet)))

def analyze(tweet):
    return {'text':tweet.text,
            'sentiment':to_blob(tweet.text).sentiment,
            '_id':tweet.id,
            'datetime':tweet.created_at
            }
  
QUEUE_NAME = 'analyze_this'

if __name__ == '__main__':
    queue.work(QUEUE_NAME)
    