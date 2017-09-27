# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:41:21 2017

@author: HP
"""

from pymongo import MongoClient
import json
#import os

#os.getcwd()
#DEFAULT_DATA_PATH = os.path.abspath(os.path.join(os.path.dirname('__file__'), 'Packages','pymongo'))
#os.chdir(DEFAULT_DATA_PATH)


# creating connectioons for communicating with Mongo DB
client = MongoClient('localhost:27017')
db = client.twitter_stream

record1=db.twitter_collection
pages=open("multijsonobject.json","r")
json_data = [json.loads(page) for page in pages]
#json_data

for item in json_data:
    record1.insert(item)



