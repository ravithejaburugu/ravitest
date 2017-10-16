# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:17:15 2017

@author: ANSHUL
"""

import logging
import requests
import threading
from bs4 import BeautifulSoup
from config import mongo_config
from mongoDBConnection import make_mongo_connection


class ScrapyExtractor():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)

    def performScraping(self, scrapeURLs, i):
        """Iterates each URL to scrape and collect News articles."""

        for source in scrapeURLs:

            scrape_url = scrapeURLs[source]

            logging.info("RSS feed of " + source + "[" + scrape_url + "]")

            # Create new thread.
            i += 1
            scrape_thread = scrapeThread(i, source, i, scrape_url)
            scrape_thread.start()
        return i


class scrapeThread(threading.Thread):

    def __init__(self, threadID, name, counter, url):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url

    def run(self):
        print "Starting " + self.name
        self.scrapeAndSave(self.name, self.url)
        print "Exiting " + self.name

    def scrapeAndSave(self, source, feedURL):

        r = requests.get(feedURL)
        data = r.text

        # parse fetched data using beatifulsoup
        soup = BeautifulSoup(data)

        rows = soup.find_all("tr", {"class": "nn"})

        # Creating Mongo Collection
        mongo_colln = make_mongo_connection(source)
        index_name = mongo_config.get('mongo_index_name')
        if index_name not in mongo_colln.index_information():
            mongo_colln.create_index(index_name, unique=False)

        for col in rows:
            td = col.find_all("td")
            for url in td:
                link = url.find('a', href=True)
                if link:
                    original_link = link['href']
                    logging.info("Scraping " + source + "[" + original_link
                                 + "]")

                    response = requests.get(original_link)

                    object1 = {source: response.content}

                    # Inserting feed data into Mongo Collection
                    mongo_colln.insert_one(object1)
                    object1.clear
