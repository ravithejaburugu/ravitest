# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:25:49 2017

@author: RAVITHEJA
"""

import os

RSS_FEED_URLS = {
        "thomson_reuters": "http://feeds.reuters.com/reuters/INbusinessNews",
        "wall_street_journal": "http://www.wsj.com/xml/rss/3_7031.xml",
        "financial_times": "https://www.openft.org/searches/083bb4149bf03104c4549dcbc929b428e8f98c84.rss", # need API KEY
        "cnbc": "https://www.cnbc.com/id/10000664/device/rss/rss.html",
        "cnn_money": "http://rss.cnn.com/rss/money_latest.rss",
        "morning_star": "http://feeds.feedburner.com/morningstar/glkd",
        "rtt_news": "http://www.rttnews.com/RSS/Todaystop.xml",
        "seeking_alpha": "https://seekingalpha.com/sector/financial.xml",
        "yahoo_finance": "https://finance.yahoo.com/rss/topstories",
        "motley_fool": "http://culture.fool.com/feed/",
        "zacks_investment": "http://feed.zacks.com/commentary/AllStories/rss",
        }

SITE_MAP_URLS = {
        "bloomberg": "https://www.bloomberg.com/robots.txt",
        "market_watch": "http://www.marketwatch.com/robots.txt",
        "forbes": "https://www.forbes.com/robots.txt",
        "ceic_data": "https://www.ceicdata.com/robots.txt",
        }

SCRAPY_URLS = {
        "finviz": "https://finviz.com/news.ashx",
        }


argument_config = {
    'rss_feed_urls': os.getenv('RSS_FEED_URLS', RSS_FEED_URLS),
    'site_map_urls': os.getenv('SITE_MAP_URLS', SITE_MAP_URLS),
    'scrapy_urls': os.getenv('SCRAPY_URLS', SCRAPY_URLS),
}

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', 'localhost:27017'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False),
    'requires_auth': os.getenv('REQUIRES_AUTH', 'false'),
    'mongo_username': os.getenv('MONGO_USER', 'ravithejab@gmail.com'),
    'mongo_password': os.getenv('MONGO_PASSWORD', 'sl03pois!'),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'dbadmin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'MONGODB-CR'),
    'db_name': os.getenv('MONGO_DB_NAME', 'finnews2'),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'csrt'),
}
