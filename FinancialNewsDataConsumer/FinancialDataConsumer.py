# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: RAVITHEJA
"""
import logging
from config import argument_config
from kafka import KafkaConsumer
from mongoDBConnection import initialize_mongo, insert_into_mongo


kafka_broker_uri = argument_config.get('kafka_broker_uri')

                       


def main():
    """Initiate the Financial news extraction functionality.
    To make calls to RSS feed parser, Sitemap parser, Scrapy extractor and
    API calls, if any."""

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    # Fetching URLs from Config file.
    

def kafkaConsumerToMongo():
    #take all feed name from config file its in dict in config.
    #use each name at a time and make a loop to complete the below flow.
    try:
        consumer = KafkaConsumer(feedName, bootstrap_servers=[kafka_broker_uri],auto_offset_reset='earliest',
                         enable_auto_commit=False)
        mongo_colln = initialize_mongo(feedName)
        print feedName
        for message in consumer:
            feedObject = {feedName : message}
            if insert_into_mongo(mongo_colln, feedObject):
                    logging.info("Inserted "+feedName+" data to Mongo successfully")
                    feedObject.clear
        
    except:
         logging.info("Error while loading to consumer/mongo: "+feedName)
         pass
            
            

if __name__ == '__main__':
    main()
