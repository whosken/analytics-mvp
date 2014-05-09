#!/usr/bin/python
# -*- coding: utf-8 -*-

import deepcopy
import textblob

import db
import queue

to_blob = textblob.Blobber()

def work(tweet):
    return db.save(analyze(to_blob(tweet)))

def analyze(blob):
    blob = blobber(tweet)
    result = copy.deepcopy(tweet)
    result['sentiment'] = blob.sentiment
    return result
  
QUEUE_NAME = 'analyze_this'

if __name__ == '__main__':
    queue.work(QUEUE_NAME)