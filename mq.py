#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis
import rq

import config

def get_redis():
    return redis.from_url(config.load().get('REDIS_URL') or 'redis://localhost:6379')

def get_queue():
    return rq.Queue('feed_queue', connection=get_redis())
  
QUEUE = get_queue()

def put(tweet):
    return QUEUE.put(tweet)
  
def pop():
    return QUEUE.pop()
  
