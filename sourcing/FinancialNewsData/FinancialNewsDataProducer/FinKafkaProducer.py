# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:22:38 2017

@author: RAVITHEJA
"""

import logging
import json
from config import argument_config
from kafka import KafkaProducer
from kafka.errors import KafkaError


class finKafkaProducer():
    """Helper class to associate news feeds from Extractor to couple with
    Kafka and write to Topics using Kafka Producer."""

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)
        kafka_broker_uri = argument_config.get('kafka_broker_uri')

        # initializing single Kafka producer instance.
        self.producer = KafkaProducer(bootstrap_servers=[kafka_broker_uri],
                                      value_serializer=lambda v:
                                          json.dumps(v).encode('utf-8'))

    def kafkaSend(self, feedName, part_url, response):
        """Sends the message to the given Kafka topic."""
        json_data = json.dumps({part_url: response})

        try:
            # Kafka producer writing Post/Webpage content to Kafka Topics.
            self.producer.send(feedName, key=feedName,
                               value=json.loads(json_data))
            self.producer.flush()
            logging.info("Kafka sending FEED :: " + feedName)
        except KafkaError as ke:
            logging.info("KafkaError in producer:- " + ke)
        except:
            logging.info("KafkaTimeoutError in kafkaProducer for: " + feedName)
