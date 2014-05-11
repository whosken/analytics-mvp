#!/usr/bin/python
# -*- coding: utf-8 -*-

import textblob
import datetime

import queue
import db

to_blob = textblob.Blobber()

def work():
    tweets,finished = queue.pop(100)
    db.save(*map(analyze, tweets))
    finished()

def analyze(tweet):
    created_at = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    return {'text':tweet['text'],
            'sentiment':to_blob(tweet['text']).sentiment,
            '_id':unicode(tweet['id']),
            'datetime':[created_at.year,
                        created_at.month,
                        created_at.day,
                        created_at.hour,
                        created_at.minute,
                        created_at.second
                        ]
            }

if __name__ == '__main__':
    while True:
        work()
