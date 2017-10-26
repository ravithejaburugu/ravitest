"""
Created on Thu Oct 12 12:16:53 2017

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


class SitemapParser():
    def __init__(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s \
                            %(module)s.%(funcName)s %(message)s',
                            level=logging.INFO)
        self.kafkaProducer = finKafkaProducer()
        self.mongo_colln = initialize_mongo()

    def crawlSiteMapXML(self, source, sitemap_url):
        """Crawls the SiteMap XMLs and Fetches the HTML pages,
        to send to Kafka Topic."""

        # Proces each .xml urls from robots.txt and return html object.
        index_response = requests.get(sitemap_url)
        index_root = etree.fromstring(index_response.content)
        logging.info(source + " has " + str(len(index_root)) + " XML URLs")

        # Process all sub .xml urls available,stored in list

        index_loc_list = []
        for i, sitemap in enumerate(index_root):
            index_children = sitemap.getchildren()
            index_loc = index_children[0].text
            index_loc_list.append(index_loc)

        for idx_loc in index_loc_list:
            if index_loc.split(".")[-1] == "xml":
                urlset_response = requests.get(index_loc)
                urlset_locs = etree.fromstring(urlset_response.content)

                logging.info("Processing the URL: " + str(i)
                             + "(" + str(len(urlset_locs)) + " URLs)")

                # Process all sub .xml urls list,returns html object for mongo
                self.loopRootURLSet(source, urlset_locs)
            else:
                logging.info("Sitemap index_loc (not xml) - " + index_loc)
                metadata_cursor = self.mongo_colln.find({source: index_loc})
                if metadata_cursor.count() == 0:
                    self.sendToKafka(source, index_loc)
                else:
                    logging.info("Duplicate data Skipped")

    def loopRootURLSet(self, source, rootURLSets):
        for urlset_loc in rootURLSets:
            children = urlset_loc.getchildren()
            final_url = children[0].text
            logging.info("urlset_loc final_url - " + final_url)
            metadata_cursor = self.mongo_colln.find({source: final_url})
            if metadata_cursor.count() == 0:
                self.sendToKafka(source, final_url)
            else:
                logging.info("Duplicate data Skipped")

    def unzipSiteMapURL(self, source, sitemap_url):
        """Exctracts zip format URLs to fetch Post URLs."""

        # Process the zip url from robot.txt and store in mongo
        sitemap_xml = self.decompress_stream(sitemap_url)

        tree = etree.parse(sitemap_xml)
        root = tree.getroot()

        logging.info("The number of gz tags: " + str(len(root)))
        locs = []
        for sitemap in root:
            children = sitemap.getchildren()
            locs.append(children[0].text)      # 23 urls

        for i, loc in enumerate(locs):
            if loc.split(".")[-1] == "gz":
                sub_sitemap_xml = self.decompress_stream(loc)

                sub_tree = etree.parse(sub_sitemap_xml)
                sub_root = sub_tree.getroot()

                logging.info(str(i) + " The processing url: " + loc)
                logging.info("Final URLs at " + loc.split("/")[-1] + " are "
                             + str(len(sub_root)))

                self.loopRootURLSet(source, sub_root)
            elif loc.split(".")[-1] == "xml":
                self.crawlSiteMap(source, loc)

            else:
                logging.info("Its neither gz nor xml. Please check the format")

    def decompress_stream(self, sitemap_url):
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

    def sendToKafka(self, source, final_url):
        session = requests.Session()
        final_response = session.get(final_url, allow_redirects=True)
        logging.info("To KafkaProducer :: [" + source + "] " + final_url)

        if final_response.status_code == 200:
            self.kafkaProducer.kafkaSend(source, final_url,
                                         final_response.content)
        else:
            logging.info(str(final_response.status_code))
        time.sleep(3)
        session.close()
