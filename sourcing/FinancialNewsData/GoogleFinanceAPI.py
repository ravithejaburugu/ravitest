# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:00:57 2017

@author: ANSHUL
"""


import json
import requests
import demjson
from finsymbols.symbols import get_sp500_symbols
from finsymbols.symbols import get_nyse_symbols
from finsymbols.symbols import get_amex_symbols
from finsymbols.symbols import get_nasdaq_symbols
from config import mongo_config
from mongoDBConnection import make_mongo_connection
from bs4 import BeautifulSoup
#from urllib.request import Request, urlopen
from urllib2 import Request, urlopen


mongo_colln = make_mongo_connection('google_news')

index_name = mongo_config.get('mongo_index_name')
if index_name not in mongo_colln.index_information():
    mongo_colln.create_index(index_name, unique=False)


googleFinanceKeyToFullName = {
    u'id'     : u'ID',
    u't'      : u'StockSymbol',
    u'e'      : u'Index',
    u'l'      : u'LastTradePrice',
    u'l_cur'  : u'LastTradeWithCurrency',
    u'ltt'    : u'LastTradeTime',
    u'lt_dts' : u'LastTradeDateTime',
    u'lt'     : u'LastTradeDateTimeLong',
    u'div'    : u'Dividend',
    u'yld'    : u'Yield',
    u's'      : u'LastTradeSize',
    u'c'      : u'Change',
    u'cp'      : u'ChangePercent',
    u'el'     : u'ExtHrsLastTradePrice',
    u'el_cur' : u'ExtHrsLastTradeWithCurrency',
    u'elt'    : u'ExtHrsLastTradeDateTimeLong',
    u'ec'     : u'ExtHrsChange',
    u'ecp'    : u'ExtHrsChangePercent',
    u'pcls_fix': u'PreviousClosePrice'
}

def buildUrl(symbols):
    symbol_list = ','.join([symbol for symbol in symbols])
    # a deprecated but still active & correct api
    return 'http://finance.google.com/finance/info?client=ig&q=' \
        + symbol_list

def buildNewsUrl(symbol, qs='&start=0&num=1000'):
   return 'http://www.google.com/finance/company_news?output=json&q=' \
        + symbol + qs

def request(symbols):
    url = buildUrl(symbols)
    req = Request(url)
    resp = urlopen(req)
    # remove special symbols such as the pound symbol
    content = resp.read().decode('ascii', 'ignore').strip()
    content = content[3:]
    return content

def requestNews(symbol):
    url = buildNewsUrl(symbol)
    print "url: ", url
    req = Request(url)
    resp = urlopen(req)
    content = resp.read()

    content_json = demjson.decode(content)

    #print "total news: ", content_json['total_number_of_news']

    article_json = []
    news_json = content_json['clusters']
    for cluster in news_json:
        for article in cluster:
            if article == 'a':
                article_json.extend(cluster[article])
    for url in article_json:
        #soup = BeautifulSoup(url['u'])
        response = requests.get(url['u'])
        object = {'googleFinanceNews' : response.content}
        mongo_colln.insert_one(object)
        object.clear
        print("Loading Google News into Mongo")
        
    return article_json

def replaceKeys(quotes):
    global googleFinanceKeyToFullName
    quotesWithReadableKey = []
    for q in quotes:
        qReadableKey = {}
        for k in googleFinanceKeyToFullName:
            if k in q:
                qReadableKey[googleFinanceKeyToFullName[k]] = q[k]
        quotesWithReadableKey.append(qReadableKey)
    return quotesWithReadableKey

def getQuotes(symbols):
    
    rsp = requests.get('https://finance.google.com/finance?q='+symbols+'&output=json')
    #KAFKA IS LEFT
    if rsp.status_code in (200,):
        fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
        object = {symbols : fin_data}
        mongo_colln.insert_one(object)
        object.clear
        print("Loading Google Stock data into Mongo")
       

def getNews(symbol):
    return requestNews(symbol);

if __name__ == '__main__':
    symbols = get_sp500_symbols() + get_nyse_symbols() + get_amex_symbols() + get_nasdaq_symbols()
    
    for a in symbols:
        try:
            json.dumps(getNews(a['symbol']), indent=2)
            json.dumps(getQuotes(a['symbol']), indent=2)   
        except:
            continue

