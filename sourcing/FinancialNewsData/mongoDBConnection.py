# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:44:42 2017

@author: RAVITHEJA
"""

from uuid import uuid1
from pymongo import MongoClient
from config import mongo_config


def make_mongo_connection(col_name):
    print("col_name --> "+col_name)
    client = MongoClient(mongo_config.get('mongo_uri'),
                         ssl=mongo_config.get('ssl_required'))
    if mongo_config.get('requires_auth') == 'true':
        client.the_database.authenticate(mongo_config.get('mongo_username'),
                                         mongo_config.get('mongo_password'),
                                         source=mongo_config.get(
                                                 'mongo_auth_source'),
                                         mechanism=mongo_config.get(
                                                 'mongo_auth_mechanism')
                                         )
    db = client[mongo_config.get('db_name')]
    col = db[col_name]

    # The code below is to ensure that the collection exists,
    # and can therefore have an index created on it
    test_uuid = str(uuid1())
    col.insert_one({'uuid': test_uuid})
    col.delete_one({'uuid': test_uuid})
    
    print(col)
    return col
