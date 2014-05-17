#!/usr/bin/python
# -*- coding: utf-8 -*-

import twython

import config
import queue
  
def get_streamer():
    key = config.get('TWITTER.KEY','TWITTER_KEY')
    key_secret = config.get('TWITTER.KEY_SECRET','TWITTER_KEY_SECRET')
    token = config.get('TWITTER.TOKEN','TWITTER_TOKEN')
    token_secret = config.get('TWITTER.TOKEN_SECRET','TWITTER_TOKEN_SECRET')
    return TwitterStreamer(key, key_secret, token, token_secret)
  
class TwitterStreamer(twython.TwythonStreamer):
    def on_success(self, data):
        queue.push(data)
        
    def on_error(self, status_code, data):
        print status_code
  
  
if __name__ == '__main__':
    stream = get_streamer()
    while True:
        stream.statuses.filter(track='Godzilla')
    