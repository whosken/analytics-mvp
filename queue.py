#!/usr/bin/python
# -*- coding: utf-8 -*-

import iron_mq
import json

import config

def get_client():
    credentials = config.load().get('IRONIO') or {}
    return iron_mq.IronMQ(project_id=config.get('IRONIO.PROJECT'),
                    token=config.get('IRONIO.TOKEN'))

def get_queue(queue_name=None):
    return MQ.queue(queue_name or 'analyze_this')

def push(*messages):
    return get_queue().post(messages)

def pop(max=10):
    queue = get_queue()
    messages = queue.get(max)['messages']
    delete_messages = lambda : queue.delete_multiple(*[m['id'] for m in messages])
    return [json.loads(m) for m in messages], delete_messages
  