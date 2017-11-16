# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import logging
from config import argument_config, mongo_config
from mongoDBConnection import initialize_mongo, insert_into_mongo
from ckanForMetadata import insert_into_ckan


def persistFinData(source, dataset_url, json_data):
    """Collects the Quandl JSON response data and inserts into mongo collection
    and updates CKAN."""

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    ckan_host = argument_config.get('ckan_host')
    owner_org = argument_config.get('owner_org')
    api_key = argument_config.get('api_key')
    publisher = argument_config.get('publisher')
    mongo_uri = mongo_config.get('mongo_uri')

    try:
        feedObject = {source: json_data}
        logging.info("Initializing Mongo for :::::: " + source)
        mongo_colln = initialize_mongo(source)
        try:
            logging.info("Inserting into " + source)
            inserted = insert_into_mongo(mongo_colln, feedObject)
            if inserted:
                logging.info("Inserted " + source + " data to MongoDB")

                # Maintain metadata for the inserted data.
                try:
                    meta_mongo_colln = initialize_mongo("METADATA")
                    meta_feedObj = {source: dataset_url}
                    insert_into_mongo(meta_mongo_colln, meta_feedObj)
                except:
                    logging.error("Error while adding to Metadata")

                # Maintain CKAN information for each Web source.
                try:
                    insert_into_ckan(ckan_host, api_key, publisher,
                                     mongo_uri, source, owner_org)
                    logging.info("Updated CKAN for " + source)
                except:
                    logging.error("Error while loading to CKAN.")
            else:
                logging.info(source + " data not saved in MongoDB")
        except:
            logging.error("Error while loading to MongoDB.")
        finally:
            feedObject.clear
    except:
        logging.error("Error while Initializing Mongo.")
        pass
