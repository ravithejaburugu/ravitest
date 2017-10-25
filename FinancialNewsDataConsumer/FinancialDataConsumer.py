# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: ANSHUL
"""

import logging
from config import argument_config
from kafka import KafkaConsumer
from mongoDBConnection import initialize_mongo, insert_into_mongo
from ckanForMetadata import insert_into_ckan


def main():
    """Initiate the Financial news extraction functionality.
    To make calls to RSS feed parser, Sitemap parser, Scrapy extractor and
    API calls, if any."""

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    kafka_topics = argument_config.get('kafka_topics')
    kafka_broker_uri = argument_config.get('kafka_broker_uri')
    ckan_host = argument_config.get('ckan_host')
    api_key = argument_config.get('api_key')
    publisher = argument_config.get('publisher')

    try:
        consumer = KafkaConsumer(*kafka_topics,
                                 bootstrap_servers=[kafka_broker_uri],
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False)
        for message in consumer:
            source = message.key
            print source
            mongo_colln = initialize_mongo(source)
            feedObject = {source: message.value}

            try:
                if insert_into_mongo(mongo_colln, feedObject):
    
                    insert_into_ckan(ckan_host, api_key, publisher,
                                     source, feedObject)
    
                    logging.info("Inserted " + source + " data to MongoDB")
                    feedObject.clear
            except:
                logging.info("Error while loading to Mongo/CKAN ")
                continue
    except IOError:
        logging.info("Error while loading to consumer/Mongo ")
        pass


if __name__ == '__main__':
    main()
