# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:07:02 2017

@author: RAVITHEJA
"""

import time
import logging
import json
import os
from FinDataPersist import persistFinData
from mongoDBConnection import initialize_mongo, insert_into_mongo

# mongo_colln = initialize_mongo(mongo_config.get('col_name'))
feed_count = {}


def main():
    """Initiates the Financial news extraction from Quandl using API calls."""

    t1 = time.time()

    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s :: %(message)s',
                        level=logging.INFO)

    # Fetching URLs from CSV file.
    with open('Quandl_csv1.csv', 'r') as csv_file:
        csv_data = csv_file.readlines()
        i = 4
        for line in csv_data:
            if i == 0:
                break
            else:
                i = i - 1

            last_ele = line.split(',')[-1]
            if last_ele.startswith('http'):
                dataset_url = last_ele.replace('zWss8KsbxmzVojqwVr9E',
                                               'o7xFVwAfWTqCsY5mgMGh')
                logging.info("dataset_url :: " + dataset_url)
                try:
                    time.sleep(3)
                    resp_data = os.popen("curl " + dataset_url).read()
                    json_data = json.loads(resp_data)
                    # logging.info(json_data)
                    dataset_source = line.split(',')[0]
                    dataset_source = dataset_source.strip().replace(' ', '_')\
                                                            .replace('\"','')
                    if not dataset_source:
                        dataset_source = "others"
                    persistFinData(dataset_source,
                                   dataset_url.replace('o7xFVwAfWTqCsY5mgMGh',''),
                                   json_data)
                except:
                    continue

    logging.info("Total time taken to fetch data from Quandl : " + str(t1))


if __name__ == '__main__':
    main()
