# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:48:44 2017
@author: ADMIN
"""

import os

HASHTAGS = ["WSJ", "business", "Forbes", "FT", "Reuters", "nytimes",
            "TheStreet", "TheEconomist", "WSJMarkets", "CNNMoney",
            "MarketWatch", "YahooFinance", "jimcramer", "bySamRo",
            "BrianSozzi", "TruthGundlach", "MarketFolly", "Carl_C_Icahn",
            "ReformedBroker", "Northman Trader", "Samir_Madani"]

argument_config = {
    'consumer_key': os.getenv('CONSUMER_KEY', 'f6V9MManq18hH7KFSVSsbMSEU'),
    'consumer_secret': os.getenv('CONSUMER_SECRET', '4dtVe6I0SyBDcG6XwCUU7mSeAVDRbRrGkToHOYOycxyd6mt8VN'),
    'access_token': os.getenv('ACCESS_TOKEN', '912282441276055552-8ZR1KVdWtbNzlgHkQlPzQtYJqgGrOZd'),
    'access_token_secret': os.getenv('ACCESS_TOKEN_SECRET', 'X2axJM3ETUfu2wEBjl2XWZ5Dr9yy5j3luwm4FkWWJFRun'),
    'twitter_hashtags': os.getenv('TWITTER_HASHTAGS', HASHTAGS),
    'kafka_broker_uri': os.getenv('KAFKA_BROKER_URI', 'localhost:9092'),
    'kafka_topic': os.getenv('KAFKA_TOPIC', 'TWITTERHANDLE'),
    'source_method': os.getenv('SOURCE_METHOD', 'mongo') #kafka/mongo
}

mongo_config = {
    'requires_auth': os.getenv('REQUIRES_AUTH', 'false'),
    'mongo_uri': os.getenv('MONGO_URI', 'localhost:27017'),
    'mongo_username': os.getenv('MONGO_USER', ''),
    'mongo_password': os.getenv('MONGO_PASSWORD', ''),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'dbadmin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'MONGODB-CR'),
    'db_name': os.getenv('MONGO_DB_NAME', 'twitter'),
    'col_name': os.getenv('MONGO_COL_NAME', 'tweet'),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'anshul'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False)
}