# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import os

argument_config = {
    'ckan_host': os.getenv('CKAN_HOST', 'http://40.71.214.191:80'),
    'api_key': os.getenv('CKAN_API_KEY', '3474fcd0-2ebc-4036-a60a-8bf77eea161f'),
    'publisher': os.getenv('PUBLISHER', 'Randomtrees'),
    'owner_org': os.getenv('OWNER_ORG', 'securities-exchange-commission'),
}

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', 'localhost:27017'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False),
    'requires_auth': os.getenv('REQUIRES_AUTH', 'false'),
    'mongo_username': os.getenv('MONGO_USER', ''),
    'mongo_password': os.getenv('MONGO_PASSWORD', ''),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'dbadmin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'MONGODB-CR'),
    'db_name': os.getenv('MONGO_DB_NAME', 'quan6'),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', '_hash'),
    'col_name': os.getenv('MONGO_COL_NAME', 'METADATA'),
}
