# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import time
import logging
import json
import os
from config import argument_config
from FinDataPersist import persistFinData
from urllib2 import Request, urlopen


def main():
    """Initiates the Financial news extraction from Quandl using API calls."""

    t1 = time.time()

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    quandl_apikey = argument_config.get('quandl_apikey')

    # Fetching URLs from CSV file.
    with open('Quandl_csv1.csv', 'r') as csv_file:
        for line in csv_file.readlines():
            last_ele = filter(None, reversed(map(str.strip, line.split(','))))[0]
            if last_ele.startswith('http'):
                dataset_url = last_ele + quandl_apikey

                dataset_source = line.split(',')[0]
                logging.info("Fetching data of : " + dataset_source)
                try:
                    time.sleep(3)
                    resp_data = os.popen(dataset_url).read()
                    json_data = json.loads(resp_data)

                    dataset_source = dataset_source.strip().replace(' ', '_')\
                                                           .replace('\"', '')
                    if not dataset_source:
                        dataset_source = "others"
                    persistFinData(dataset_source, last_ele, json_data)
                except:
                    continue

    logging.info("Total time taken to fetch data from Quandl : " + str(t1))


if __name__ == '__main__':
    main()
