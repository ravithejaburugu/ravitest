# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 13:16:53 2017

@author: Admin
"""


import os


argument_config = {
    'azure_account_name': os.getenv('AZURE_ACCOUNT_NAME'),
    'azure_account_key': os.getenv('AZURE_ACCOUNT_KEY'),
	'container': os.getenv('CONTAINER'),
    'dataset': os.getenv('DATASET'),
    'ckan_host': os.getenv('CKAN_HOST'),
    'ckan_key': os.getenv('CKAN_KEY'),
	'owner_org': os.getenv('OWNER_ORG')
}
