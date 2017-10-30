# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:03:16 2017

@author: RAVITHEJA
"""

import requests
import zlib
import logging
import time
from functools import partial
from lxml import etree
from StringIO import StringIO
from FinKafkaProducer import finKafkaProducer
from mongoDBConnection import initialize_mongo
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup


class SitemapParser():
    """Helper to parse the various SiteMap URLs taken from the robots.txt files
    of Financial News Web sources."""

    def __init__(self, source, auth_id, auth_pwd):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)
        self.source = source
        self.auth_id = auth_id
        self.auth_pwd = auth_pwd

        self.mongo_colln = initialize_mongo()
        self.kafkaProducer = finKafkaProducer()

        self.url_count = 0

    def sitemapCrawler(self, sitemap_url):
        """Crawls through sitemap URLs, for webpage URLs. Their content
        is written to Kafka Topics by Kafka Producer."""

        if sitemap_url.split(".")[-1] == "gz":
            sitemap_xml = self.decompress_stream(sitemap_url)
            tree = etree.parse(sitemap_xml)
            root = tree.getroot()

            locs = dict([(sno, (sitemap.getchildren()[0]).text)
                        for sno, sitemap in enumerate(root)])

            for loc in locs:
                locs[loc] = self.sitemapCrawler(locs[loc])

        elif sitemap_url.split(".")[-1] == "xml":
            logging.info("got xml.")

            sitemap_xml = requests.get(sitemap_url)
            index_root = etree.fromstring(sitemap_xml.content)

            xlocs = dict([(sno, (sitemap.getchildren()[0]).text)
                         for sno, sitemap in enumerate(index_root)])

            for loc in xlocs:
                xlocs[loc] = self.sitemapCrawler(xlocs[loc])

        else:
            # Check and hold from duplicate data capture.
            metadata_cursor = self.mongo_colln.find({self.source: sitemap_url})
            if metadata_cursor.count() == 0:
                self.sendToKafka(self.source, sitemap_url)
            else:
                logging.info("Duplicate data Skipped")
        return self.url_count

    def decompress_stream(self, sitemap_url):
        """Decompresses the zip files in .gz format."""
        zip_response = requests.get(sitemap_url, stream=True)
        rraw = zip_response.raw

        READ_BLOCK_SIZE = 1024 * 8
        sitemap_xml = StringIO()

        # Compiling decompress object
        d = zlib.decompressobj(16 + zlib.MAX_WBITS)

        for chunk in iter(partial(rraw.read, READ_BLOCK_SIZE), ''):
            sitemap_xml.write(d.decompress(chunk))

        # offsetting the current position to the absolute file position.
        sitemap_xml.seek(0)
        return sitemap_xml

    def sendToKafka(self, source, source_url):
        """Interfaces Kafkaproducer to write messages into Kafka Topics."""
        try:

            if self.auth_id and self.auth_pwd:
                session = requests.Session()
                wsj_response = session.get(source_url, allow_redirects=True)
                soup = BeautifulSoup(wsj_response.content)
                div_elements = soup.findAll('div',
                                            attrs={'class': 'carousel-item locked'}
                                            )
                for div in div_elements:
                    final_url = div.find('a')['href']
                    session = requests.Session()
    
                    final_response = session.get(final_url,
                                                 auth=HTTPBasicAuth(self.auth_id,
                                                                    self.auth_pwd))
                    if final_response.content:
                        self.kafkaProducer.kafkaSend(source, source_url,
                                                     final_response.content)
                        logging.info("To KafkaProducer :: [" + source + "] "
                                     + source_url)
            else:
                session = requests.Session()
                final_response = session.get(source_url, allow_redirects=True)
                if final_response.content:
                    self.kafkaProducer.kafkaSend(source, source_url,
                                                 final_response.content)
                    logging.info("To KafkaProducer :: [" + source + "] "
                                 + source_url)

            self.url_count += 1
            time.sleep(3)
        except:
            logging.error("Error while request.get in Sitemap.")
            raise
        finally:
            session.close()
