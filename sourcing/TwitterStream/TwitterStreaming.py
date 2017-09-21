# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:15:15 2017

@author: ANSHUL
"""

import logging
import tweepy
import json
import datetime
import requests
import re
from bs4 import BeautifulSoup


class TwitterStreamListener(tweepy.StreamListener):
    """This is the stream listener, resposible for listeneing from Twitter
    and receiving data using countinuously Streaming."""

    def on_data(self, response):
        """ This method is invoked on obtaining response data from the
        Twitter stream """

        # parsing response to JSON format
        json_resp = json.loads(response+"\n")

        filename = "twitter_" + str(datetime.date.today()).replace('-', '') +\
            ".json"

        # Writing the Twitter response tweets to a file
        with open(filename, 'a+') as response_file:
            json.dump(json_resp, response_file, sort_keys=True, indent=4)

        # show progress
        logging.info("Obtained a tweet from Twitter stream. \
                     CTRL+C to terminate the streaming.")
        return True

    def on_error(self, status):
        """ Prints the response error status. """
        print status


def getTwitterIds(twitter_accounts):
    twitter_ids = []

    for ta in twitter_accounts:
        getIdUrl = "http://gettwitterid.com/?submit=GET+USER+ID&user_name="+ta
        r = requests.get(getIdUrl)
        soup = BeautifulSoup(r.content, "html.parser")

        p_list = soup.find_all('p')
        for p_val in p_list:
            if 'Twitter User ID:' in p_val:
                id_line = p_list[p_list.index(p_val)+1]
                id_val = re.split('[< >]', str(id_line))[2]
                twitter_ids.append(id_val)

    return twitter_ids


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s \
                        %(module)s.%(funcName)s %(message)s',
                        level=logging.INFO)

    # Authentication details as arguments.
    azure_account_name = argument_config.get('azure_account_name')
    azure_account_key = argument_config.get('azure_account_key')
    azure_container = argument_config.get('azure_container')
    ckan_host = argument_config.get('ckan_host')
    ckan_api_key = argument_config.get('ckan_key')

    consumer_key = "sCmEgB3NYwt4Pnolar1CgDqNj"
    consumer_secret = "mllcum0wjpb6KdyHV0lqJRzH6FSgpDVB3MSzNQMOx9wKt3cSae"
    access_token = "909762256350601216-eqFBd8WIW7PmHsru3VlR6eS7Mg5dnXT"
    access_token_secret = "uTjwzMo7jEfkRVWyA9dSJAQ6mePBGEcmjgCVa0lAIDB23"

    listener = TwitterStreamListener()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # accessing StreamingAPI using tweepy to Authenticate as Step 1.
    stream = tweepy.Stream(auth, listener)
    logging.info("Twitter authenticated.")

    # Hashtag to twitter pages
    twitter_account_tags = ['WSJ',
                            'business',
                            'Forbes',
                            'FT',
                            'Reuters',
                            'nytimes',
                            'TheStreet',
                            'TheEconomists',
                            # 'TheEconomists',
                            'WSJMarkets',
                            'CNNMoney',
                            'MarketWatch',
                            'YahooFinance',
                            'jimcramer',
                            'bySamRo',
                            'BrianSozzi',
                            'TruthGundlach',
                            'MarketFolly',
                            'Carl_C_Icahn',
                            'ReformedBroker',
                            'Northman Trader',
                            'Samir_Madani']

    twitter_ids = getTwitterIds(twitter_account_tags)
    print twitter_ids

    while True:
        try:
            stream.filter(follow=twitter_ids)
            logging.info("Twitter Streaming initiated...")
        except:
            continue


if __name__ == '__main__':
    main()
