# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:16:31 2017

@author: RAVITHEJA
"""

import logging
import feedparser
from config import mongo_config
from mongoDBConnection import make_mongo_connection


class RSSFeedParser():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)

    def parseFeed(self, rss_feed_urls):
        print("parseFeed")
        for rss_feed in rss_feed_urls:
            print(rss_feed, rss_feed_urls[rss_feed])
            feed = feedparser.parse(rss_feed_urls[rss_feed])
            
            feed = str(feed).replace('\'', '"')
            print(feed)

            rss_object = {rss_feed: feed}

            logging.info("Loading Consumer message in Mongo")

            mongo_colln = make_mongo_connection(rss_feed)
            index_name = mongo_config.get('mongo_index_name')
            if index_name not in mongo_colln.index_information():
                mongo_colln.create_index(index_name, unique=False)

            mongo_colln.insert_one(rss_object)
            print("INSERTED SUCCESFULLY")
            rss_object.clear
            
            break
