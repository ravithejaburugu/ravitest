# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import os

argument_config = {
    'quandl_apikey': os.getenv('QUANDL_APIKEY', ''),
    'ckan_host': os.getenv('CKAN_HOST', ''),
    'api_key': os.getenv('CKAN_API_KEY', ''),
    'publisher': os.getenv('PUBLISHER', ''),
    'owner_org': os.getenv('OWNER_ORG', ''),
}

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', ''),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False),
    'requires_auth': os.getenv('REQUIRES_AUTH', ''),
    'mongo_username': os.getenv('MONGO_USER', ''),
    'mongo_password': os.getenv('MONGO_PASSWORD', ''),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', ''),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', ''),
    'db_name': os.getenv('MONGO_DB_NAME', ''),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', ''),
    'col_name': os.getenv('MONGO_COL_NAME', ''),
}
