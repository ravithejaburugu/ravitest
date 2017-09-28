# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:15:15 2017
@author: ANSHUL
"""

import sys
import math
import logging
import tweepy
import json
import time
import requests
import re
from kafka import KafkaProducer, KafkaConsumer
from bs4 import BeautifulSoup
from mongoconnection import make_mongo_connection
from config import mongo_config, argument_config
import os


class TwitterStreamListener(tweepy.StreamListener):
    """This is the stream listener, resposible for listeneing from Twitter
    and receiving data using countinuously Streaming."""

    def __init__(self, hashtags, twitter_ids, kafka_broker_uri, kafka_topic):
        self.t = 60
        self.hashtags = hashtags
        self.twitter_ids = twitter_ids
        self.kafka_topic = kafka_topic
        self.siesta = 0
        self.nightnight = 0
        
        try:
            self.producer = KafkaProducer(bootstrap_servers=[kafka_broker_uri])
   
        except:
            logging.error("Error while creating Kafka producer : ")

        


    def on_data(self, response):
        """ This method is invoked on obtaining response data from the
        Twitter stream """

        # parsing response to JSON format
        json_resp = json.loads(response)

        if (json_resp["retweeted"] is 'true') or ('RT @' in json_resp["text"]):
            return True
        tweet = {}
        user_mentions = json_resp["entities"]["user_mentions"]
        user_mention = user_mentions[len(user_mentions)-1]

        if user_mention["screen_name"] in self.hashtags:
            tweet[user_mention["screen_name"]] = json.dumps(json_resp)
            # Writing Tweet to Kafa Topics into producer

            self.producer.send(self.kafka_topic, bytes(tweet))
            self.producer.flush()
            logging.info("-- TWEET :: " + json_resp["text"])
            
        
        return True
        
			
    def on_error(self, status_code):
        if status_code == 420:
            sleepy = 60 * math.pow(2, self.siesta)
            logging.warn("A reconnection attempt will occur in {0} minutes, due to ERROR: {1}."
                         .format(str(sleepy/60), str(status_code)))

            time.sleep(sleepy)
            self.siesta += 1
        elif status_code == 401:
            logging.error("INVALID KEY/ACCESS TOKEN(S).")
            sys.exit()
        else:
            sleepy = 5 * math.pow(2, self.nightnight)
            logging.warn("A reconnection attempt will occur in {0} seconds, due to ERROR: {1}."
                         .format(str(sleepy), str(status_code)))
            time.sleep(sleepy)
            self.nightnight += 1
        return True
 
class consumer():
    
    def __init__(self, kafka_broker_uri, kafka_topic):
        self.kafka_topic = kafka_topic
        self.col = make_mongo_connection(mongo_config.get('col_name'))
        try:
            self.consumer = KafkaConsumer(bootstrap_servers=[kafka_broker_uri],
                     auto_offset_reset='earliest')
        except:
            logging.error("Error while creating Kafka Consumer : ")        

        
    def consumerToMongo(self, kafka_topic):
        self.consumer.subscribe(kafka_topic)
       
        for message in self.consumer:
            f = open("consumer.json", "w")
            with f as consume:
                 
                json.dump(message, consume)
            #f.close()
            pages=open("consumer.json","r")
            json_data = [json.loads(page) for page in pages]  
            for item in json_data:
                print'c'
                self.col.insert_one(item)
                print'd'
        pages.close()     
        os.remove(pages)

def getTwitterIds(twitter_accounts):
    """ Fetches the twitter Ids for the Twitter accounts based on Hashtags."""

    twitter_ids = []
    getIdUrl = "http://gettwitterid.com/?submit=GET+USER+ID&user_name={0}"

    for ta in twitter_accounts:
        r = requests.get(getIdUrl.format(ta))
        soup = BeautifulSoup(r.content, "html.parser")
        p_list = soup.find_all('p')
        for p_val in p_list:
            if 'Twitter User ID:' in p_val:
                id_line = p_list[p_list.index(p_val)+1]
                id_val = re.split('[< >]', str(id_line))[2]
                twitter_ids.append(id_val)
    return twitter_ids



if __name__ == '__main__':
    """ Twitter Streaming program execution begins from here."""

    # Declaring logger.
    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s %(message)s',
                        level=logging.INFO)

    # Collecting Authentication and other details from arguments.
    consumer_key = argument_config.get('consumer_key')
    consumer_secret = argument_config.get('consumer_secret')
    access_token = argument_config.get('access_token')
    access_token_secret = argument_config.get('access_token_secret')
    twitter_hashtags = argument_config.get('twitter_hashtags')
    kafka_broker_uri = argument_config.get('kafka_broker_uri')
    kafka_topic = argument_config.get('kafka_topic')
    source_method = argument_config.get('source_method')

    # OAuth authentication functionality for Twitter
    twitter_auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    twitter_auth.set_access_token(access_token, access_token_secret)

    # Fetching Ids for Twitter accounts.
    twitter_ids = getTwitterIds(twitter_hashtags)
    if source_method == 'kafka':
        try:
            # Instantiating listener class.
            listener = TwitterStreamListener(twitter_hashtags, twitter_ids,
                                             kafka_broker_uri, kafka_topic)
        except:
            logging.error("Error while creating Stream Listener : ")
    
    
    # Accessing StreamingAPI using tweepy to Authenticate as Step 1.
        stream = tweepy.Stream(twitter_auth, listener)
        logging.info("Twitter authenticated.")
        
    
        while True:
            try:
                # Initializing Streaming for the given Twitter Accounts
                stream.filter(follow=twitter_ids)
                #TwitterConsumer( kafka_broker_uri, kafka_topic )
                logging.info("Twitter Streaming initiated...")
            except:
                continue
        
    elif source_method == 'mongo':
        try:
            consume = consumer(kafka_broker_uri,kafka_topic)
            consume.consumerToMongo(kafka_topic)
        except:
            raise
            #logging.error("Error while calling consumer class : ")

         
