# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: RAVITHEJA
"""

from lxml import etree
import time
import logging
import threading
import feedparser
import requests
import demjson
import os
import json
from config import argument_config, mongo_config
from bs4 import BeautifulSoup
from mongoDBConnection import initialize_mongo, insert_into_mongo
from finsymbols.symbols import get_sp500_symbols, get_nyse_symbols
from finsymbols.symbols import get_amex_symbols, get_nasdaq_symbols
from urllib2 import Request, urlopen
from SiteMap import SitemapParser


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
    i = 0

    """ RSSFeedParsing begins. """
    for rss_feed_name in rss_feed_urls:
        rss_feed_url = rss_feed_urls[rss_feed_name]
        logging.info("RSS feed of " + rss_feed_name + "[" + rss_feed_url + "]")
        # Creating new thread.
        i += 1
        feed_thread = ThreadClass(i, rss_feed_name, i, rss_feed_url, 'rss')
        feed_thread.start()

    """ SitemapParsing begins. It fetches all sitmap urls from robots.txt and
        filters the zip, xml urls.
    for source in site_map_urls:
        print(source, site_map_urls[source])
        robots_url = site_map_urls[source]
        # Creating new thread.
        i += 1
        scrape_thread = ThreadClass(i, source, i, robots_url, 'sitemap')
        scrape_thread.start()"""

    """ Scraping begins. 
    for source in scrapy_urls:
        scrape_url = scrapy_urls[source]
        logging.info("RSS feed of " + source + "[" + scrape_url + "]")
        # Creating new thread.
        i += 1
        scrape_thread = ThreadClass(i, source, i, scrape_url, 'scrape')
        scrape_thread.start()"""

    """ Google finance News extraction begins.
    all_fin_symbols = get_sp500_symbols() + get_nyse_symbols() + get_amex_symbols() + get_nasdaq_symbols()

    logging.info("RSS feed of Google News")
    i += 1
    # Creating new thread.
    gnews_thread = ThreadClass(i, 'googlenews', i, all_fin_symbols,
                               'googlenews')
    gnews_thread.start()"""

    """ Google Stocks extraction begins.
    logging.info("RSS feed of Google Stocks")
    i += 1
    # Creating new thread.
    gstocks_thread = ThreadClass(i, 'googlestocks', i, all_fin_symbols,
                                 'googlestocks')
    gstocks_thread.start()"""

    logging.info("Total time taken :: " + str(time.time() - t1))


class ThreadClass(threading.Thread):

    def __init__(self, threadID, name, counter, source_url, feedtype):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.source_url = source_url
        self.feedtype = feedtype

    def run(self):
        print "Starting " + self.name

        if self.feedtype == 'rss':
            self.parseAndSave(self.name, self.source_url)
        elif self.feedtype == 'sitemap':
            self.crawlAndScrape(self.name, self.source_url)
        elif self.feedtype == 'scrape':
            self.scrapeAndSave(self.name, self.source_url)
        elif self.feedtype == 'googlenews':
            self.getGoogleNews(self.name, self.source_url)
        elif self.feedtype == 'googlestocks':
            self.getGoogleQuotes(self.name, self.source_url)

        print "Exiting " + self.name

    def parseAndSave(self, feedName, feedURL):
        feed = feedparser.parse(feedURL)
        entries = feed['entries']
        for e in entries:
            print e['link']
            r = requests.get(feedURL)
            data = r.content
            print data
            # parse fetched data using beatifulsoup
            #soup = BeautifulSoup(data, "html.parser")
            #print "+++++++++++++++SOUP++++++++++++++++++"
            #print soup
            #rows = soup.find_all("tr", {"class": "nn"})

           # break
            
    def crawlAndScrape(self, source, robots_url):
        result = os.popen("curl " + robots_url).read()
        sitemapParser = SitemapParser()
        for line in result.split("\n"):
            if line.startswith('Sitemap'):    # this is for allowed url
                sitemap_url = line.split(': ')[1].split(' ')[0]
                print "The Sitemap url from robot.txt ::: {0} "\
                    .format(sitemap_url)
                if sitemap_url.split(".")[-1] != "gz":
                    sitemapParser.crawlSiteMap(source, sitemap_url)
                else:
                    sitemapParser.unzipURL(source, sitemap_url)
                        
    def scrapeAndSave(self, feedName, feedURL):
        r = requests.get(feedURL)
        data = r.text
        # parse fetched data using beatifulsoup
        soup = BeautifulSoup(data)
        rows = soup.find_all("tr", {"class": "nn"})

        # Creating Mongo Collection
        mongo_colln = initialize_mongo(feedName)

        for col in rows:
            td = col.find_all("td")
            for url in td:
                link = url.find('a', href=True)
                if link:
                    original_link = link['href']
                    logging.info("Scraping " + feedName + "[" + original_link
                                 + "]")
                    response = requests.get(original_link)
                    object1 = {feedName: response.content}

                    # Inserting feed data into Mongo Collection
                    mongo_colln.insert_one(object1)
                    object1.clear

    def getGoogleNews(self, feedName, finsymbols):
        base_url = 'http://www.google.com/finance/company_news?'\
                    + 'output=json&start=0&num=1000&q='
        for symbol in finsymbols:
            symbol = symbol['symbol']
            url = base_url + symbol
            req = Request(url)
            resp = urlopen(req)
            content = resp.read()
            content_json = demjson.decode(content)
            # print "total news: ", content_json['total_number_of_news']
            logging.info("Loading Google News into Mongo : " + symbol)
            article_json = []
            news_json = content_json['clusters']
            for cluster in news_json:
                for article in cluster:
                    if article == 'a':
                        article_json.extend(cluster[article])
            for url in article_json:
                response = requests.get(url['u'])
                gnews_object = {'googleFinanceNews': response.content}
                mongo_colln = initialize_mongo(feedName)
                if insert_into_mongo(mongo_colln, gnews_object):
                    logging.info("INSERTED SUCCESSFULLY.")

            # json.dumps(article_json, indent=2)

    def getGoogleQuotes(self, feedName, finsymbols):
        base_url = 'https://finance.google.com/finance?output=json&q='
        for symbol in finsymbols:
            symbol = symbol['symbol']
            rsp = requests.get(base_url + symbol)

            # TODO: Create KAFKA Topic
            if rsp.status_code in (200,):
                logging.info("Loading Google Stock data into Mongo: " + symbol)
                fin_data = json.loads(rsp.content[6:-2]
                                      .decode('unicode_escape'))
                gstock_object = {symbol: fin_data}
                mongo_colln = initialize_mongo(feedName)
                if insert_into_mongo(mongo_colln, gstock_object):
                    logging.info("INSERTED SUCCESSFULLY.")


if __name__ == '__main__':
    main()
