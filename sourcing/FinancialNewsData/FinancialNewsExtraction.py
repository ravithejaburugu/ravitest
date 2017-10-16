# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:01:20 2017

@author: RAVITHEJA
"""

import time
import logging
from config import argument_config
from RSSFeed import RSSFeedParser
from SiteMap import SitemapParser
from Scrapy import ScrapyExtractor


def main():
    """Initiate the Financial news extraction functionality.
    To make calls to RSS feed parser, Sitemap parser, Scrapy extractor and
    API calls, if any."""

    t1 = time.time()

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    # Fetching URLs from Config file.
    rss_feed_urls = argument_config.get('rss_feed_urls')
    site_map_urls = argument_config.get('site_map_urls')
    scrapy_urls = argument_config.get('scrapy_urls')

    # Instantiating RSSFeedParser
    rssFeedParser = RSSFeedParser()
    i = rssFeedParser.parseFeed(rss_feed_urls)

    # Instantiating SitemapParser
    sitemapParser = SitemapParser()
    i = sitemapParser.crawlAndScrape(site_map_urls, i)

    # Instantiating ScrapyExtractor
    scrapyExtractor = ScrapyExtractor()
    i = scrapyExtractor.performScraping(scrapy_urls, i)

    logging.info("Total time taken :: " + str(time.time() - t1))


if __name__ == '__main__':
    main()
