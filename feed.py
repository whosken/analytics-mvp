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
    auth = tweepy.OAuthHandler(config.get('TWITTER.KEY','TWITTER_KEY'),
                               config.get('TWITTER.SECRET','TWITTER_SECRET'))
    auth.set_access_token(config.get('TWITTER.TOKEN','TWITTER_TOKEN'), 
                          config.get('TWITTER.TOKEN_SECRET','TWITTER_TOKEN_SECRET'))
    return tweepy.API(auth)
  
if __name__ == '__main__':
    twitter = get_twitter()
    since_id = None
    while True:
        since_id = listen(twitter, since_id)
        