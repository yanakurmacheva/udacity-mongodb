#!/usr/bin/env python
# coding: utf-8

'''
A simple data processing pipeline.
'''

import json
import os
import pprint
from pymongo import MongoClient

USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = 'test'
CONNECTION_STRING = f'mongodb+srv://{USER}:{PASSWORD}@test.hcoeu.mongodb.net/{DATABASE}?retryWrites=true&w=majority'
CHECK = True

def convert_json(pathname):
    '''Deserializes a JSON file.'''
    data = []
    for line in open(pathname):
        data.append(json.loads(line))
    return data

def check_collection(db, collection, pathname):
    '''Creates collection if it doesn't exist, otherwise
    outputs a warning message.
    '''
    if collection in db.list_collection_names():
        print('\nThis collection already exists!\n')
    else:
        data = convert_json(pathname)
        print('\nInserting data...\n')
        # flexible schema!
        print('Peek at the document structure:\n')
        pprint.pprint(data[0])
        # MongoDB creates collections implicitly
        db[collection].insert_many(data)
        print('\nDone!\n')

def unique_mentions(db, limit):
    '''Counts unique Twitter mentions made by a user.
    Returns a subset of users with the most mentions.
    '''
    pipeline = [{'$unwind': '$entities.user_mentions'},
                {'$group': {'_id': '$user.screen_name', 'mentions': {'$addToSet': '$entities.user_mentions.screen_name'}}},
                {'$unwind': '$mentions'}, {'$group': {'_id': '$_id', 'count': {'$sum': 1}}},
                {'$sort': {'count': -1}}, {'$limit': limit}]
    # aggregation operations return a cursor object
    return db.tweets.aggregate(pipeline)

client = MongoClient(CONNECTION_STRING)
db = client[DATABASE]

if CHECK:
    check_collection(db, 'tweets', 'data/twitter.json')

result = unique_mentions(db, 3)
pprint.pprint(list(result))


client.close()
