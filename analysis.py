#!/usr/bin/python
# -*- coding: utf-8 -*-

import textblob
import datetime

import queue
import db

to_blob = textblob.Blobber()

def work():
    tweets,finished = queue.pop(100)
    return db.save(map(analyze, tweets))

def analyze(tweet):
    return {'text':tweet.text,
            'sentiment':to_blob(tweet.text).sentiment,
            '_id':tweet.id,
            'datetime':[tweet.created_at.year,
                        tweet.created_at.month,
                        tweet.created_at.day,
                        tweet.created_at.hour,
                        tweet.created_at.minute,
                        tweet.created_at.second
                        ]
            }
  
QUEUE_NAME = 'analyze_this'

if __name__ == '__main__':
    while True:
        work()
    