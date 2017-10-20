# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:25:49 2017

@author: RAVITHEJA
"""

import os

SOURCES = {
        "thomson_reuters",
        "wall_street_journal",
        "financial_times",
        "cnbc",
        "cnn_money",
        "morning_star",
        "rtt_news",
        "seeking_alpha",
        "yahoo_finance",
        "motley_fool",
        "zacks_investment",
        "bloomberg",
        "market_watch",
        "forbes",
        "ceic_data",
        "finviz",
        "googleNews",
        "googlestock"
         }


argument_config = {
    'kafka_broker_uri': os.getenv('KAFKA_BROKER_URI', 'localhost:9092'),
    #'kafka_topic': os.getenv('KAFKA_TOPIC', 'twitterhandle')
}

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', 'localhost:27017'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False),
    'requires_auth': os.getenv('REQUIRES_AUTH', 'false'),
    'mongo_username': os.getenv('MONGO_USER', 'ravithejab@gmail.com'),
    'mongo_password': os.getenv('MONGO_PASSWORD', 'sl03pois!'),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'dbadmin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'MONGODB-CR'),
    'db_name': os.getenv('MONGO_DB_NAME', 'finnews2'),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'csrt'),
}