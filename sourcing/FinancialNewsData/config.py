# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:25:49 2017

@author: RAVITHEJA
"""

import os

RSS_FEED_URLS = {
        "thomson_reuters":"http://feeds.reuters.com/reuters/INbusinessNews",
        "wall_street_journal":"http://www.wsj.com/xml/rss/3_7031.xml",
        "financial_times":"https://www.openft.org/searches/083bb4149bf03104c4549dcbc929b428e8f98c84.rss", # need API KEY
        "cnbc":"https://www.cnbc.com/id/10000664/device/rss/rss.html",
        "cnn_money":"http://rss.cnn.com/rss/money_latest.rss",
        "morning_star":"http://feeds.feedburner.com/morningstar/glkd",
        "rtt_news":"http://www.rttnews.com/RSS/Todaystop.xml",
        "seeking_alpha":"https://seekingalpha.com/sector/financial.xml",
        "yahoo_finance":"https://finance.yahoo.com/rss/topstories",
        "motley_fool":"http://culture.fool.com/feed/",
        "zacks_investment_research":"http://feed.zacks.com/commentary/AllStories/rss",
        }

SITE_MAP_URLS = {
        "bloomberg":"https://www.bloomberg.com/robots.txt",
        "market_watch":"http://www.marketwatch.com/robots.txt",
        "forbes":"https://www.forbes.com/robots.txt",
        "ceic_data":"https://www.ceicdata.com/robots.txt",
        }

SCRAPY_URLS = {
        "finviz":"https://finviz.com/news.ashx",
        }


argument_config = {
    'rss_feed_urls': os.getenv('RSS_FEED_URLS', RSS_FEED_URLS.values()),
    'site_map_urls': os.getenv('SITE_MAP_URLS', SITE_MAP_URLS.values()),
    'scrapy_urls': os.getenv('SCRAPY_URLS', SCRAPY_URLS.values()),
}
