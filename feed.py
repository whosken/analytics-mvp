#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import queue
import analysis

def listen():
    tweets = poll()
    return map(enqueue, tweets)
  
def poll():
    pass
  
def enqueue(tweet):
    return (queue.get_queue(analysis.QUEUE_NAME)
            .enqueue(analysis.work, tweet))
  
if __name__ == '__main__':
    import time
  
    while True:
        if not listen():
            time.sleep(10)