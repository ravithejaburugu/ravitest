# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import logging
import ckanapi
from datetime import datetime
from config import mongo_config


def insert_into_ckan(ckan_host, api_key, publisher, mongo_uri, source,
                     owner_org):
    """"CKAN holds the meta information about the saved data of MongoDB."""

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    # Fetch config params.
    db_name = mongo_config.get('db_name')

    ckan_ckan = ckanapi.RemoteCKAN(ckan_host, apikey=api_key)

    package_name = source.lower().replace("_", "-")
    package_title = source.replace("_", " ")
    description = "Financial News from Quandl for " + package_title

    dict_additional_fields = {
            'Title': package_title,
            'Sourcing Date': datetime.now().strftime("%B %d, %Y, %H:%M"),
            'Source': source,
            'Datastore': mongo_uri,
            'Database Name': db_name,
            'Collection': source,
            'Description': description,
            }
    additional_fields = []
    for k, v in dict_additional_fields.items():
        additional_fields.append({'key': k, 'value': v})

    tags = buildTags(source)
    try:
        ckan_ckan.action.package_create(name=package_name,
                                        title=package_title,
                                        maintainer=publisher,
                                        tags=tags,
                                        notes=description,
                                        private='True',
                                        owner_org=owner_org,
                                        extras=additional_fields,
                                        )
    except:
        try:
            ckan_ckan.action.package_update(id=package_name,
                                            title=package_title,
                                            maintainer=publisher,
                                            tags=tags,
                                            notes=description,
                                            private='True',
                                            owner_org=owner_org,
                                            extras=additional_fields,
                                            )
        except:
            logging.error("CKAN package creation/updation failed: "
                          + package_name)


def buildTags(source):
    """Tags need to be customized and built separately."""
    tags = []
    tags.append({'name': source.replace("_", " ")})
    tags.append({'name': "Quandl"})
    tags.append({'name': "FinancialData"})
    return tags
