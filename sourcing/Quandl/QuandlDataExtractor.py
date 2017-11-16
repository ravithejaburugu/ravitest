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
from mongoDBConnection import initialize_mongo


def parseDataColumns(column_names, json_data_part):
    json_data_parsed = []
    for rec in json_data_part:
        json_data_parsed.append({column_names[c]: rec[c]
                                for c in range(len(column_names))})
    return json_data_parsed


def main():
    """Initiates the Financial news extraction from Quandl using API calls."""

    t1 = time.time()
    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    quandl_apikey = argument_config.get('quandl_apikey')

    # Fetching URLs from CSV file.
    with open('Quandl_csv1.csv', 'r') as csv_file:

        # Iterate once for each line in CSV file.
        for line in csv_file.readlines():

            # Reversing the comma separated string list to get the last String.
            rev_eles = filter(None, reversed(map(str.strip, line.split(','))))
            last_ele = ''
            if len(rev_eles) > 0:
                last_ele = rev_eles[0]

            # Exclude if last element is not a URL
            if last_ele.startswith('http'):

                # Append the API Key to the URL
                dataset_url = last_ele + quandl_apikey
                dataset_source = line.split(',')[0]
                logging.info("Fetching data of : " + dataset_source + " from "
                             + dataset_url)

                try:
                    # Wait is needed to avoid reaching Quandl server
                    # restrictions for free account.
                    time.sleep(3)

                    # removing spaces for mongo collection name.
                    source_colln = dataset_source.strip()\
                                                 .replace(' ', '_')\
                                                 .replace('\"', '')
                    if not source_colln:
                        source_colln = "others"
                        
                    # Check if Collection already exists in MongoDB.
                    meta_mongo_colln = initialize_mongo("METADATA")
                    metadata_cursor = meta_mongo_colln.find({source_colln:
                                                            last_ele})
                    print metadata_cursor.count()
                    if metadata_cursor.count() == 0:
                        resp_data = os.popen("curl " + dataset_url).read()
                        json_data = json.loads(resp_data)
                        
                        json_data["dataset"]["data"] = parseDataColumns(
                                json_data["dataset"]["column_names"],
                                json_data["dataset"]["data"])

                        persistFinData(source_colln, last_ele, json_data)
                    else:
                        logging.info("Collection already exists for " +
                                     dataset_source)
                except:
                    continue

    logging.info("Total time taken to fetch data from Quandl : " +
                 str(int(time.time() - t1)) + " seconds")


if __name__ == '__main__':
    main()
