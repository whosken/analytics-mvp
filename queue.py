#!/usr/bin/python
# -*- coding: utf-8 -*-

import iron_mq
import requests.exceptions

import json

import config

def get_client():
    return iron_mq.IronMQ(
        project_id=config.get('IRONIO.PROJECT','IRON_MQ_PROJECT_ID'),
        token=config.get('IRONIO.TOKEN','IRON_MQ_TOKEN'))
        
def get_queue():
    return get_client().queue('analyze_this')

def push(*messages):
    return get_queue().post(*map(json.dumps, messages))

def pop(max=10):
    queue = get_queue()
    messages = queue.reserve(max)['messages']
    message_ids = [(m['id'],m['reservation_id']) for m in messages]
    delete_messages = get_delete_messages(queue, message_ids)
    return [json.loads(m['body']) for m in messages], delete_messages

def get_delete_messages(queue, message_ids):
    def delete_messages():
        for message_id, reservation_id in message_ids:
            try:
                queue.delete(message_id, reservation_id)
            except requests.exceptions.HTTPError as error:
                print error
                print error.response.text
    return delete_messages