# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:16:31 2017

@author: RAVITHEJA
"""

import logging
import threading
import feedparser
from mongoDBConnection import insert_into_mongo


class RSSFeedParser():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s :: %(message)s',
                            level=logging.INFO)

    def parseFeed(self, rss_feed_urls):
        """Iterates each RSS to pass the URL for parsing Feeds."""

        i = 0
        for rss_feed_name in rss_feed_urls:
            rss_feed_url = rss_feed_urls[rss_feed_name]

            logging.info("RSS feed of " + rss_feed_name + "[" + rss_feed_url
                         + "]")
            # Create new thread.
            i += 1
            feed_thread = rssThread(i, rss_feed_name, i, rss_feed_url)
            feed_thread.start()
        return i


class rssThread(threading.Thread):

    def __init__(self, threadID, name, counter, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url

    def run(self):
        print "Starting " + self.name
        self.parseAndSave(self.name, self.url)
        print "Exiting " + self.name

    def parseAndSave(self, feedName, feedURL):
        feed = feedparser.parse(feedURL)

        feed = str(feed).replace('\'', '"')
        logging.info(feed)

        rss_object = {feedName: feed}

        logging.info("Loading Feed in MongoDB...")

        if insert_into_mongo(feedName, rss_object):
            logging.info("INSERTED SUCCESSFULLY.")
