
# coding: utf-8

# #### Name : Download the dbpedia data into a Azure Blob
# #### Author : spaturu
# #### Date :  07/31/2017

# In[1]:

from azure.storage.blob import BlockBlobService, ContentSettings, PublicAccess, AppendBlobService
import wget
import requests
import os
from os import path
from bs4 import BeautifulSoup
import mimetypes
from datetime import datetime
mimetypes.init()
import urllib


# In[2]:

account_name = str(input('Enter UserName for Azure :'))
account_key  = str(input('Enter Key for Azure :'))
container    = str(input('Enter the Container :'))
block_blob_service = BlockBlobService(account_name = account_name,account_key  = account_key)
append_blob_service = AppendBlobService(account_name = account_name,account_key  = account_key)


# In[3]:

try:
    if block_blob_service == True:
            print('connection successful!')
except Exception as e:
            print('Please make sure the account name and key are correct.', e)


# In[4]:

if block_blob_service.exists(container):
    pass
else:
    block_blob_service.create_container(container)


# In[5]:

urls = {'ontology' :['http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.owl',
           'http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.nt']}
#         'wikipedia' :['https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-pages-articles-multistream.xml.bz2',
#             'https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-pages-articles-multistream-index.txt.bz2',
#              'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
#             'http://www.gnu.org/copyleft/fdl.html'],
#          'datasets' :['http://downloads.dbpedia.org/2016-10/core-i18n/en/'],
#         'nlp' :['http://model.dbpedia-spotlight.org/latest_data/en.tar.gz'],
#         'dataid':['http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.json',
#          'http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.ttl']}


# In[12]:

metadata ={}
azure_urls=[]
for blob in urls:
    print(blob)
    for url in urls[blob]:
        print(url)
        r = requests.get(url,stream=True)
        file_name = url.split("/")[-1]
        with open(file_name, 'wb') as data:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    data.write(chunk)
        block_blob_service.create_blob_from_path(path.join(container,blob),
                              data.name,
                              file_name ,
                              content_settings=ContentSettings(content_type=mimetypes.guess_type('./%s' %url.split("/")[-1])[0]))
        print('uploading file to '+''+blob+' '+'in a '+ container)
        os.remove(data.name)
        download_url = block_blob_service.make_blob_url(path.join(container, blob),data.name)
        azure_urls.append(download_url)
    metadata[blob]= azure_urls
    metadata['Title'] = 'Dbpedia'+'-'+blob
    metadata['Publisher'] = 'SiddarthaP'
    metadata['Created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata['version'] = "2016-10"
    metadata[ "Container"] = container
    metadata['SourceType'] = [url.split(".")[-1] for url in azure_urls]
    print(metadata)


# In[62]:

import ckanapi
import requests
import sys
import pprint
ckan = ckanapi.RemoteCKAN('http://40.71.214.191','3474fcd0-2ebc-4036-a60a-8bf77eea161f' )
ckan.action.package_create(name = response,title ='ontology')


# In[61]:

import urllib
import urllib.parse
import json
import pprint
data_string = urllib.parse.quote(json.dumps(metadata)).encode("utf-8")
request = urllib.request.Request(
    'http://40.71.214.191/api/3/action/package_create')
request.add_header('Authorization', '3474fcd0-2ebc-4036-a60a-8bf77eea161f')
request.add_header('Content-Type','application/x-www-form-urlencoded')
response = urllib.request.urlopen(request, data_string)
assert response.code == 200
response_dict = json.loads(response.read())
assert response_dict['success'] is True
created_package = response_dict['result']
pprint.pprint(created_package)


# In[ ]:

archive_url = "http://downloads.dbpedia.org/2016-10/core-i18n/en/"
def get_links():
     
    # create response object
    r = requests.get(archive_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'html5lib')
     
    # find all links on web-page
    links = soup.findAll('a')
 
    # filter the link sending with .mp4
    data_links = [archive_url + link['href'] for link in links if link['href'].endswith('bz2')]
 
    return data_links


# In[ ]:

data_links = get_links()


# In[ ]:

print(data_links)


# In[ ]:

def download_data(data_links):
 
    for link in data_links:
 
        '''iterate through all links in data_links
        and download them one by one'''
         
        # obtain filename by splitting url and getting 
        # last string
        file_name = link.split('/')[-1]   
 
        #print ("Downloading file:%s"%file_name)
         
        # create response object
        r = requests.get(link, stream = True)
         
        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
         
        print ("%s downloaded!\n"%file_name)
 
    print ("All data downloaded!")
    return


# In[ ]:

download_data(data_links)

