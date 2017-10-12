# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:16:53 2017

@author: RAVITHEJA
"""

import logging
import requests
from bs4 import BeautifulSoup


class SitemapParser():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)


    def crawlAndScrape(self, scrapeURLs):
        
        for url in scrapeURLs:
            r = requests.get(url)
            text = r.text
            soup = BeautifulSoup(text)
            

    