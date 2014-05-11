#!/usr/bin/python
# -*- coding: utf-8 -*-

import textblob
import datetime

import queue
import db

to_blob = textblob.Blobber()

def work():
    tweets,finished = queue.pop(100)
    if not tweets: return
    db.save(*map(analyze, tweets))
    finished()
    return len(tweets)

def analyze(tweet):
    created_at = datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
    sentiment = to_blob(tweet['text']).sentiment.polarity
    return {'text':tweet['text'],
            'sentiment':get_sentiment(tweet['text']),
            '_id':unicode(tweet['id']),
            'datetime':[created_at.year,
                        created_at.month,
                        created_at.day,
                        created_at.hour,
                        created_at.minute,
                        created_at.second
                        ]
            }
  
def get_sentiment(text):
    sentiment = to_blob(text).sentiment.polarity
    if sentiment > 0: return 'pos'
    if sentiment < 0: return 'neg'
    return 'neu'

    
if __name__ == '__main__':
    import time    
    while True:
        if not work():
            print 'sleeping...'
            time.sleep(2)
