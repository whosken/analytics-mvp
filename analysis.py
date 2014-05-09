#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import mq
import db

def work():
    tweets = mq.pop()
    db.save(map(analyze,tweets))

def analyze(tweet):
    pass
  

import textblob
import redis
import cPickle
  
def train():
    pass
  
def save(model):
    pass
  
def load():
    pass
  
  