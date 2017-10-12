# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:17:15 2017

@author: RAVITHEJA
"""

import logging
import requests
from bs4 import BeautifulSoup
from config import mongo_config
from mongoDBConnection import make_mongo_connection


class ScrapyExtractor():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)


    def performScraping(self, scrapeURLs):
        for source in scrapeURLs:
            print(source, scrapeURLs[source])

            r = requests.get(scrapeURLs[source])
            data = r.text
        
            # parse fetched data using beatifulsoup
            soup = BeautifulSoup(data)
            
            rows = soup.find_all("tr", {"class": "nn"})

            
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
                        print original_link
                        
                        req = requests.get(original_link)

                        object1 = {source: req.content}
                    
                        mongo_colln.insert_one(object1)
                        object1.clear
                
