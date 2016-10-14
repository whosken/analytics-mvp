#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
import pymongo.errors

import config

HOST = config.get('MONGO','MONGODB_URI','mongodb://localhost:27017')
DB_NAME = pymongo.uri_parser.parse_uri(HOST).get('database')
COLLECTION_NAME = 'tweets'

collection = pymongo.MongoClient(HOST)[DB_NAME][COLLECTION_NAME]

def save(*results):
    bulk = collection.initialize_ordered_bulk_op()
    for result in results:
        bulk.find({'_id':result['_id']}).upsert().replace_one(result)
    try:
        bulk.execute()
    except pymongo.errors.BulkWriteError as error:
        print error.details

def latest_sentiments(since=None):
    latest = since
    pipeline = [
        {'$group':{
            '_id':'$sentiment',
            'count':{'$sum':1},
            'latest':{'$max':'$datetime'}
            }}
        ]
    if since:
        pipeline = [{'$match':{'datetime':{'$gte':since}}}] + pipeline
    results = list(collection.aggregate(pipeline))
    sentiments = dict((r['_id'],r['count']) for r in results)
    lastest = max(r['latest'] for r in results)
    return sentiments, latest
