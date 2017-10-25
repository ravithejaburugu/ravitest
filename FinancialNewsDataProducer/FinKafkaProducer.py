# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:22:38 2017

@author: RAVITHEJA
"""

import logging
from config import argument_config
from kafka import KafkaProducer


class finKafkaProducer():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)
        kafka_broker_uri = argument_config.get('kafka_broker_uri')
        self.producer = KafkaProducer(bootstrap_servers=[kafka_broker_uri])

    def kafkaSend(self, feedName, response):
        """Sends the message to the given Kafka topic."""
        try:
            # Kafka producer writing Post/Webpage content to Kafka Topics.
            self.producer.send(feedName, key=feedName, value=response)
            self.producer.flush()
            logging.info("-- FEED :: " + feedName)
        except ValueError:
            logging.info("Issue in kafka Producer for: " + feedName)
