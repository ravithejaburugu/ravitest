# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:25:49 2017

@author: RAVITHEJA
"""

import os


RSS_FEED_URLS = {
        #"thomson_reuters": "http://feeds.reuters.com/reuters/INbusinessNews",
        #"wall_street_journal": "http://www.wsj.com/xml/rss/3_7031.xml",
        #"cnbc": "https://www.cnbc.com/id/10000664/device/rss/rss.html",
        #"cnn_money": "http://rss.cnn.com/rss/money_latest.rss",
        #"morning_star": "http://feeds.feedburner.com/morningstar/glkd",
        #"rtt_news": "http://www.rttnews.com/RSS/Todaystop.xml",
        #"seeking_alpha": "https://seekingalpha.com/sector/financial.xml",
        #"yahoo_finance": "https://finance.yahoo.com/rss/topstories",
        #"motley_fool": "http://culture.fool.com/feed/",
        #"zacks_investment": "http://feed.zacks.com/commentary/AllStories/rss",
        }

SITE_MAP_URLS = {
        "bloomberg": "https://www.bloomberg.com/robots.txt",
        #"market_watch": "https://www.marketwatch.com/robots.txt",
        #"forbes": "https://www.forbes.com/robots.txt",
        #"the_street": "https://www.thestreet.com/robots.txt",
        #"msci_dataset": "https://www.msci.com/robots.txt",
        #"ceic_dataset": "https://www.ceicdata.com/robots.txt",
        }

HISTORICAL_SITEMAP_URLS = {
        #"wall_street_journal": "https://www.wsj.com/robots.txt",
        #"cnbc": "https://www.cnbc.com/robots.txt",
        #"cnn_money": "http://money.cnn.com/robots.txt",
        #"rtt_news": "http://www.rttnews.com/robots.txt",
        #"seeking_alpha": "https://seekingalpha.com/robots.txt",
        #"zacks_investment": "https://www.zacks.com/robots.txt",
        
        #"motley_fool": "http://culture.fool.com/robots.txt",
        }

SCRAPY_URLS = {
        #"finviz": "https://finviz.com/news.ashx",
        }


argument_config = {
    'kafka_broker_uri': os.getenv('KAFKA_BROKER_URI', 'localhost:9092'),

    'rss_feed_urls': os.getenv('RSS_FEED_URLS', RSS_FEED_URLS),
    'site_map_urls': os.getenv('SITE_MAP_URLS', SITE_MAP_URLS),
    'scrapy_urls': os.getenv('SCRAPY_URLS', SCRAPY_URLS),
    'historical_urls': os.getenv('HISTORICAL_URLS', HISTORICAL_SITEMAP_URLS),

    'ft_api_key': os.getenv('FT_API_KEY', '7hnme32uuvku4r9zp47kf5x9'),
    'ft_auth_id': os.getenv('FT_AUTH_ID', 'vavasarala@randomtrees.com'),
    'ft_auth_pwd': os.getenv('FT_AUTH_PWD', ''),
    'wsj_auth_id': os.getenv('WSJ_AUTH_ID', 'vavasarala@randomtrees.com'),
    'wsj_auth_pwd': os.getenv('WSJ_AUTH_PWD', 'welcome123'),
}

mongo_config = {
    'mongo_uri': os.getenv('MONGO_URI', 'localhost:27017'),
    'ssl_required': os.getenv('MONGO_SSL_REQUIRED', False),
    'requires_auth': os.getenv('REQUIRES_AUTH', 'false'),
    'mongo_username': os.getenv('MONGO_USER', ''),
    'mongo_password': os.getenv('MONGO_PASSWORD', ''),
    'mongo_auth_source': os.getenv('MONGO_AUTH_SOURCE', 'dbadmin'),
    'mongo_auth_mechanism': os.getenv('MONGO_AUTH_MECHANISM', 'MONGODB-CR'),
    # db_name needs to be same as consumer code, for checking duplicates.
    'db_name': os.getenv('MONGO_DB_NAME', 'finnews_all0'),
    'col_name': os.getenv('MONGO_COL_NAME', 'METADATA'),
    'mongo_index_name': os.getenv('MONGO_INDEX_NAME', 'csrt'),
}
