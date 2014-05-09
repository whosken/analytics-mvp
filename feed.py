#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy

import config
import queue
import analysis
import db

def listen(twitter, since_id=None):
    tweets = twitter.search('#PyConAPAC',since_id=since_id)
    db.save({'docs':map(enqueue, tweets)})
    return tweets.since_id
  
def get_twitter():
    credentials = config.load().get('TWITTER')
    auth = tweepy.OAuthHandler(credentials.get('KEY'), 
                               credentials.get('KEY_SECRET'))
    auth.set_access_token(credentials.get('TOKEN'), 
                          credentials.get('TOKEN_SECRET'))
    return tweepy.API(auth)
  
def enqueue(tweet):
    return (queue.get_queue(analysis.QUEUE_NAME)
            .enqueue(analysis.work, tweet))
  
if __name__ == '__main__':
    twitter = get_twitter()
    since_id = None
    while True:
        since_id = listen(twitter, since_id)
        