# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: ANSHUL
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

#def kafkaConsumerToMongo():
    kafka_topics = argument_config.get('kafka_topics')
    print len(kafka_topics)
#    for feedName in kafka_topics:
    try:
        consumer = KafkaConsumer(*,
                                 bootstrap_servers=[kafka_broker_uri],
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False)
        mongo_colln = initialize_mongo(feedName)
        print feedName
        for message in consumer:
            feedObject = {feedName: message}
            if insert_into_mongo(mongo_colln, feedObject):
                    logging.info("Inserted " + feedName + " data to Mongo"
                                 + " successfully")
                    feedObject.clear
        consumer.close()
    except:
        logging.info("Error while loading to consumer/mongo: " + feedName)
        pass


if __name__ == '__main__':
    main()