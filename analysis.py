#!/usr/bin/python
# -*- coding: utf-8 -*-

import textblob
import datetime

import queue

to_blob = textblob.Blobber()

def analyze(tweet):
    return {'text':tweet.text,
            'sentiment':to_blob(tweet.text).sentiment,
            '_id':tweet.id,
            'datetime':unicode(tweet.created_at)
            }
  
QUEUE_NAME = 'analyze_this'

if __name__ == '__main__':
    queue.work(QUEUE_NAME)
    