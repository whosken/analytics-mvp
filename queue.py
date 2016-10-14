#!/usr/bin/python
# -*- coding: utf-8 -*-

import iron_mq
import json

import config

client = iron_mq.IronMQ(
    project_id=config.get('IRONIO.PROJECT','IRON_MQ_PROJECT_ID'),
    token=config.get('IRONIO.TOKEN','IRON_MQ_TOKEN'))
queue = client.queue('analyze_this')

def push(*messages):
    return queue.post(*map(json.dumps, messages))

def pop(max=10):
    messages = queue.get(max)['messages']
    message_ids = [m['id'] for m in messages]
    delete_messages = get_delete_messages(queue, message_ids)
    return [json.loads(m['body']) for m in messages], delete_messages

def get_delete_messages(queue, message_ids):
    def delete_messages():
        for message_id in message_ids:
            try:
                queue.delete(message_id)
            except Exception as error:
                print error
    return delete_messages