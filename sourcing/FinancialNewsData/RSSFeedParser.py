# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:22:19 2017

@author: RAVITHEJA
"""

import feedparser

rss_urls = ["https://seekingalpha.com/sector/financial.xml",
           "http://feeds.feedburner.com/morningstar/bmyh",
           "http://feed.zacks.com/commentary/AllStories/rss",
           "http://www.wsj.com/xml/rss/3_7031.xml",
           "https://www.cnbc.com/id/10000664/device/rss/rss.html",
           "https://www.ft.com/news-feed",
           "http://culture.fool.com/feed/"]

for rss_url in rss_urls:
    print rss_url
    feed = feedparser.parse(rss_url)
    print feed
    
