#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis
import rq

import config

def get_redis():
    return redis.from_url(config.load().get('REDIS') or os.environ.get('REDISTOGO_URL') or 'redis://localhost:6379')
  
REDIS = get_redis()

def get_queue(queue_name):
    return rq.Queue(queue_name,connection=REDIS)
  
def work(*listen):
    with rq.Connection(REDIS):
        worker = rq.Worker(map(rq.Queue,listen))
        worker.work()
        