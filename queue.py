#!/usr/bin/python
# -*- coding: utf-8 -*-

import iron_mq
import json

import config

def get_client():
    return iron_mq.IronMQ(project_id=config.get('IRONIO.PROJECT'),
                          token=config.get('IRONIO.TOKEN'))

def get_queue(queue_name=None):
    return get_client().queue(queue_name or 'analyze_this')

def push(*messages):
    return get_queue().post(*map(json.dumps, messages))

def pop(max=10):
    queue = get_queue()
    messages = queue.get(max)['messages']
    message_ids = [m['id'] for m in messages]
    delete_messages = lambda : map(queue.delete, message_ids)
    return [m for m in map(try_json_loads, messages) if m], delete_messages
  
def try_json_loads(text):
    try:
        return json.loads(text)
    except TypeError as error:
        print error
    