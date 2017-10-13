# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 12:16:53 2017

@author: RAVITHEJA
"""

import requests
import zlib
import httplib2
import os
import logging
from pymongo import MongoClient
from functools import partial
from lxml import etree
from StringIO import StringIO
from bs4 import BeautifulSoup
#import robotparser


class SitemapParser():

    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)

    def crawlAndScrape(self, site_map_urls):
        #print site_map_urls
        for source in site_map_urls:
            print(source, site_map_urls[source])
            robots_url = site_map_urls[source]
            result = os.popen("curl " + robots_url).read()

            for line in result.split("\n"):
                if line.startswith('Sitemap'):    # this is for allowed url
                    print("line = "+line)
                    sitemap_url = line.split(': ')[1].split(' ')[0]
                    if sitemap_url.split(".") !="gz":
                        http_response = self.crawlSiteMap(sitemap_url)
                        self.insertMongo(source, http_response)
                    else:
                        self.unzipURL(sitemap_url)
                        

        
    def crawlSiteMap(self, sitemap_url):
        index_response = requests.get(sitemap_url) 
        index_root = etree.fromstring(index_response.content)
        #print "The number of sitemap tags are {0}".format(len(index_root))
        
        http_responses = []
        for sitemap in index_root:
            print("sitemap = ")
            print(sitemap)
            index_children = sitemap.getchildren()
            index_loc = index_children[0].text
            
            print("index_loc = "+ index_loc)
            urlset_response = requests.get(index_loc) 
            soup = BeautifulSoup(urlset_response.text)
            urlset_locs = soup.find_all("loc")
            print "The number of locs tags are {0}".format(len(urlset_locs))
            
            for urlset_loc in urlset_locs:
                final_url = urlset_loc.contents[0]
            
                http = httplib2.Http()
                http_headers, http_response = http.request(final_url, 'GET')    
                if http_headers['status'] == "200":
                    #print(http_response)
                    http_responses.append(http_response)
                    
        return http_responses
                


    def unzipURL(self, sitemap_url):
        response = requests.get(sitemap_url, stream=True)
        sitemap_xml = self.decompress_stream(response.raw)
        tree = etree.parse(sitemap_xml)
        root = tree.getroot()
        print "The number of sitemap tags are {0}".format(len(root))
        locs=[]
        for sitemap in root:
            children = sitemap.getchildren()
            print children[0].text
            locs.append(children[0].text)
            for loc in locs:
                 if loc.split(".")[-1] =="gz":
                     self.gz_urls(loc)
                        

    def decompress_stream(self, rraw):
        READ_BLOCK_SIZE = 1024 * 8
        result = StringIO()
        d = zlib.decompressobj(16 + zlib.MAX_WBITS)
        for chunk in iter(partial(rraw.read, READ_BLOCK_SIZE), ''):
            result.write(d.decompress(chunk))
        result.seek(0)
        return result

                
    def insertMongo(self, source, http_response):
        client = MongoClient()
        db = client.html
        collection = db.html
        collection.insert_one({source: http_response})

