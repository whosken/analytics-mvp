#!/usr/bin/python
# -*- coding: utf-8 -*-

import deepcopy
import textblob

import mq
import db

def work():
    blobber = textblob.Blobber()
    tweets = map(blobber, mq.pop())
    db.save(map(analyze,tweets))

def analyze(blob):
    blob = blobber(tweet)
    result = copy.deepcopy(tweet)
    result['sentiment'] = blob.sentiment
    return result
  
if __name__ == '__main__':
    while True:
        work()
        