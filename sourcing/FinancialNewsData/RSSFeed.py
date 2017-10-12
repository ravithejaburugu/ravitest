# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:16:31 2017

@author: RAVITHEJA
"""

import logging
import feedparser


class RSSFeedParser():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)


    def parseFeed(self, scrapeURLs):
        for rss_url in scrapeURLs:
            print rss_url
            feed = feedparser.parse(rss_url)
            print feed
    