# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: RAVITHEJA
"""

import time
import logging
import feedparser
import requests
import demjson
import os
import json
from config import argument_config
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
from SiteMap import SitemapParser
from finsymbols.symbols import get_sp500_symbols, get_nyse_symbols
from finsymbols.symbols import get_amex_symbols, get_nasdaq_symbols
from kafka import KafkaProducer


kafka_broker_uri = argument_config.get('kafka_broker_uri')
producer = KafkaProducer(bootstrap_servers=[kafka_broker_uri])
                       


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

    """ RSSFeedParsing begins. """
    for rss_feed_name in rss_feed_urls:
        rss_feed_url = rss_feed_urls[rss_feed_name]
        logging.info("RSS feed of " + rss_feed_name + "[" + rss_feed_url + "]")
        parseAndSave(rss_feed_name, rss_feed_url)

    """ SitemapParsing begins. It fetches all sitmap urls from robots.txt and
        filters the zip, xml urls."""
    for source in site_map_urls:
        print(source, site_map_urls[source])
        robots_url = site_map_urls[source]
        crawlAndScrape(source, robots_url, producer)

    """ Scraping begins."""
    for source in scrapy_urls:
        scrape_url = scrapy_urls[source]
        logging.info("RSS feed of " + source + "[" + scrape_url + "]")
        scrapeAndSave(source, scrape_url)

    """ Google finance News extraction begins."""
    all_fin_symbols = get_sp500_symbols() + get_nyse_symbols() + get_amex_symbols() + get_nasdaq_symbols()

    logging.info("RSS feed of Google News")
    getGoogleNews("gnews", all_fin_symbols)

    """ Google Stocks extraction begins."""
    logging.info("RSS feed of Google Stocks")
    getGoogleQuotes("gstocks", all_fin_symbols)

    logging.info("Total time taken :: " + str(time.time() - t1))


def kafkaSendProducer(feedName, response):
    try:
        # Writing Tweet to Kafa Topics into producer
        producer.send(feedName, response)
        producer.flush()
        #future = producer.send(feedName, {feedName: response})
        #result = future.get(timeout=60)
        logging.info("-- FEED :: " + feedName)
    except ValueError:
        logging.info("Issue in kafka Producer for: " + feedName)
        

def parseAndSave(feedName, feedURL):
    feed = feedparser.parse(feedURL)
    entries = feed['entries']
    for e in entries:
        response = requests.get(e['link'])
        kafkaSendProducer(feedName, response.content)
        

 
def crawlAndScrape(source, robots_url, producer):
    result = os.popen("curl " + robots_url).read()
    sitemapParser = SitemapParser(producer)
    for line in result.split("\n"):
        if line.startswith('Sitemap'):    # this is for allowed url
            sitemap_url = line.split(': ')[1].split(' ')[0]
            print "The Sitemap url from robot.txt ::: {0} "\
                .format(sitemap_url)
            if sitemap_url.split(".")[-1] != "gz":
                sitemapParser.crawlSiteMap(source, sitemap_url)
            else:
                sitemapParser.unzipURL(source, sitemap_url)


def scrapeAndSave(feedName, feedURL):
    r = requests.get(feedURL)
    data = r.text
    # parse fetched data using beatifulsoup
    soup = BeautifulSoup(data)
    rows = soup.find_all("tr", {"class": "nn"})

    for col in rows:
        td = col.find_all("td")
        for url in td:
            link = url.find('a', href=True)
            if link:
                original_link = link['href']
                logging.info("Scraping " + feedName + "[" + original_link
                             + "]")
                response = requests.get(original_link)
                kafkaSendProducer(feedName, response.content)

def getGoogleNews(feedName, finsymbols):
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
            kafkaSendProducer('googleFinanceNews', response.content)


def getGoogleQuotes(feedName, finsymbols):
    base_url = 'https://finance.google.com/finance?output=json&q='
    for symbol in finsymbols:
        symbol = symbol['symbol']
        rsp = requests.get(base_url + symbol)

        # TODO: Create KAFKA Topic
        if rsp.status_code in (200,):
            logging.info("Loading Google Stock data into Mongo: " + symbol)
            fin_data = json.loads(rsp.content[6:-2]
                                  .decode('unicode_escape'))
            kafkaSendProducer(symbol, fin_data)

if __name__ == '__main__':
    main()
