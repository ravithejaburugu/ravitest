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
    kafka_topics = argument_config.get('kafka_topic')
    #print len(kafka_topics)
#for feedName in kafka_topics:
    #topic = ', '.join(kafka_topics)
    
    try:
        consumer = KafkaConsumer(kafka_topics[0],kafka_topics[1],kafka_topics[2],kafka_topics[3],
                                 kafka_topics[4],kafka_topics[5],kafka_topics[6],kafka_topics[7],
                                 kafka_topics[8],kafka_topics[9],kafka_topics[10],kafka_topics[11],
                                 kafka_topics[12],kafka_topics[13],kafka_topics[14],kafka_topics[15],
                                 kafka_topics[16],kafka_topics[17],
                                 bootstrap_servers=[kafka_broker_uri],
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False)
        
        #print topic
        for message in consumer:
            mongo_colln = initialize_mongo(message.key)
            feedObject = {message.key: message.value}
            if insert_into_mongo(mongo_colln, feedObject):
                    logging.info("Inserted " + message.key + " data to Mongo"
                                 + " successfully")
                    feedObject.clear
        #consumer.close()
        
    except:
        logging.info("Error while loading to consumer/mongo ")
        pass
        

if __name__ == '__main__':
    main()
