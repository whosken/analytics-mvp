#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy

import config
import queue

def listen(twitter, since_id=None):
    tweets = twitter.search('#PyConAPAC OR #PyConAPAC2014',since_id=since_id)
    queue.push(tweets)
    return tweets.since_id
  
def get_twitter():
    credentials = config.load().get('TWITTER')
    auth = tweepy.OAuthHandler(credentials.get('KEY'), 
                               credentials.get('KEY_SECRET'))
    auth.set_access_token(credentials.get('TOKEN'), 
                          credentials.get('TOKEN_SECRET'))
    return tweepy.API(auth)
  
if __name__ == '__main__':
    twitter = get_twitter()
    since_id = None
    while True:
        since_id = listen(twitter, since_id)
        