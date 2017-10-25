# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:38:57 2017

@author: RAVITHEJA
"""

import time
import logging
import feedparser
import requests
import json
import demjson
import os
from config import argument_config
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen
from SiteMap import SitemapParser
from finsymbols.symbols import get_sp500_symbols, get_nyse_symbols
from finsymbols.symbols import get_amex_symbols, get_nasdaq_symbols
from FinKafkaProducer import finKafkaProducer
from requests.auth import HTTPBasicAuth


def main():
    """Initiates the Financial news extraction functionality.
    Executes RSS feed parser, Sitemap parser, Scraping and API calls."""

    t1 = time.time()

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    kafkaProducer = finKafkaProducer()
    
    # Fetching URLs from Config file.
    rss_feed_urls = argument_config.get('rss_feed_urls')
    site_map_urls = argument_config.get('site_map_urls')
    scrapy_urls = argument_config.get('scrapy_urls')
    auth_urls = argument_config.get('auth_urls')
    ft_api_key = argument_config.get('ft_api_key')

    rss_keys = rss_feed_urls.keys()


    """ SitemapParsing begins. It fetches all sitmap urls from robots.txt and
        filters the zip, xml urls."""
    for source in site_map_urls:
        if source in rss_keys:
            # TODO: Check in CKAN. If not available download the Historical data.
            pass
        robots_url = site_map_urls[source]
        logging.info("SiteMap for " + source + " from " + robots_url)
        crawlAndScrape(source, robots_url)


    """ RSSFeedParsing begins."""
    for rss_feed_name in rss_feed_urls:
        rss_feed_url = rss_feed_urls[rss_feed_name]
        logging.info("RSS feed of " + rss_feed_name + "[" + rss_feed_url + "]")
        parseAndSave(kafkaProducer, rss_feed_name, rss_feed_url)

    """ URLs with subscription using authentication."""
    for auth_item in auth_urls:
        auth_credentials = auth_urls[auth_item]
        auth_id = auth_credentials['auth_id']
        auth_pwd = auth_credentials['auth_pwd']

        if auth_id and auth_pwd:
            try:
                if auth_item == "financial-times":
                    news_url = "http://api.ft.com/content/search/v1"
                    scrapeFT(kafkaProducer, auth_item, news_url, auth_id,
                             auth_pwd, ft_api_key)
                elif auth_item == "the-wall-street-journal":
                    news_url = "https://newsapi.org/v1/articles"
                    scrapeWSJ(kafkaProducer, auth_item, news_url, auth_id,
                              auth_pwd)
            except:
                logging.warn("Problem while scraping " + auth_item)
                continue
        else:
            logging.warn("Subscription not found for: " + auth_item)


    """ Scraping begins."""
    for source in scrapy_urls:
        scrape_url = scrapy_urls[source]
        logging.info("RSS feed of " + source + "[" + scrape_url + "]")
        scrapeAndSave(source, scrape_url)

    all_fin_symbols = get_sp500_symbols() + get_nyse_symbols() + get_amex_symbols() + get_nasdaq_symbols()

    """ Google finance News extraction begins."""
    logging.info("Google Finance News...")
    getGoogleNews("googleFinanceNews", all_fin_symbols)

    """ Google Stocks extraction begins."""
    logging.info("Google Live Stocks...")
    getGoogleQuotes("googleStocks", all_fin_symbols)

    """Yahoo finance stock prices."""
    logging.info("Yahoo Finance Stocks...")
    getYahooStocks("yahooStocks", all_fin_symbols)

    logging.info("Total time taken :: " + str(time.time() - t1))


def scrapeWSJ(kafkaProducer, feedname, news_url, auth_id, auth_pwd):
    querystring = {"source": feedname,
                   "sortBy": "top",
                   "apiKey": "67c7663f07af4c388e2734118ffa6b17"}
    auth_response = requests.request("GET", news_url, params=querystring)
    js = json.loads(auth_response.content)
    for url in js['articles']:
        feed_response = requests.get(url['url'],
                                     auth=HTTPBasicAuth(auth_id, auth_pwd))
        if feed_response.status_code == 200:
            kafkaProducer.kafkaSend(feedname, feed_response.content)


def scrapeFT(kafkaProducer, feedname, news_url, auth_id, auth_pwd, ft_api_key):
    payload = "{\r\n\t\"queryString\": \"sections:\\\"Financials\\\"\",\r\n\t\"resultContext\" : {\r\n\t\t \"aspects\" :[  \"title\",\"lifecycle\",\"location\",\"summary\",\"editorial\" ]\r\n\t}\r\n}"
    headers = {'x-api-key': ft_api_key}
    response = requests.request("POST", news_url, data=payload,
                                headers=headers)
    js = json.loads(response.content)
    for url in js['results']:
        res = url['results']
        for loc in res:
            loc_url = loc['location']['uri']
            print loc_url
            feed_response = requests.get(loc_url,
                                         auth=HTTPBasicAuth(auth_id, auth_pwd))
            if feed_response.status_code == 200:
                kafkaProducer.kafkaSend(feedname, feed_response.content)


def parseAndSave(kafkaProducer, feedName, feedURL):
    feed = feedparser.parse(feedURL)
    entries = feed['entries']
    for e in entries:
        response = requests.get(e['link'])
        kafkaProducer.kafkaSend(feedName, response.content)


def crawlAndScrape(source, robots_url):
    result = os.popen("curl " + robots_url).read()

    sitemapParser = SitemapParser()
    for line in result.split("\n"):
        if line.startswith('Sitemap'):    # this is for allowed url
            sitemap_url = line.split(': ')[1].split(' ')[0]
            print sitemap_url
            logging.info("Extracting SiteMap: " + sitemap_url)

            # for XML formats in Sitemap
            if sitemap_url.split(".")[-1] == "xml":
                sitemapParser.crawlSiteMapXML(source, sitemap_url)

            # for gz formats in Sitemap
            elif sitemap_url.split(".")[-1] == "gz":
                sitemapParser.unzipSiteMapURL(source, sitemap_url)

            # for HTML formats in Sitemap
            elif sitemap_url.split(".")[-1] == "html":
                pass

            # for other unknown formats
            else:
                pass


def scrapeAndSave(kafkaProducer, feedName, feedURL):
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
                kafkaProducer.kafkaSend(feedName, response.content)


def getGoogleNews(kafkaProducer, feedName, finsymbols):
    base_url = 'http://www.google.com/finance/company_news?output=json'\
                + '&start=0&num=1000&q='
    for symbol in finsymbols:
        resp = urlopen(Request(base_url + symbol['symbol']))
        content_json = demjson.decode(resp.read())
        logging.info(symbol['symbol'], content_json['total_number_of_news'])

        article_json = []
        for cluster in content_json['clusters']:
            if 'a' in cluster:
                article_json.extend(cluster['a'])
        for article_url in article_json:
            logging.info(article_url['u'])
            response = requests.get(article_url['u'])
            kafkaProducer.kafkaSend(feedName, response.content)
        break


def getGoogleQuotes(kafkaProducer, feedName, finsymbols):
    base_url = 'https://finance.google.com/finance?output=json&q='
    for symbol in finsymbols:
        symbol = symbol['symbol']
        rsp = requests.get(base_url + symbol)

        if rsp.status_code in (200,):
            logging.info("Writing Google Stock data (to Topic): " + symbol)
            kafkaProducer.kafkaSend(feedName, rsp.content)
        break


def getYahooStocks(kafkaProducer, feedName, all_fin_symbols):
    for fin_symbol in all_fin_symbols:
        sym = fin_symbol['symbol']
        # base_url = 'http://finance.yahoo.com/d/quotes.csv?f=sb2b3jk&s=' + sym
        base_url = "https://finance.yahoo.com/quote/" + sym + "?p=" + sym
        rsp = requests.get(base_url)

        if rsp.status_code in (200,):
            print rsp.content
            logging.info("Writing Yahoo Stock data (to Topic): " + sym)
            kafkaProducer.kafkaSend(feedName, rsp.content)
        break


if __name__ == '__main__':
    main()
