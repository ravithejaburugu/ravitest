
# coding: utf-8

# #### Name : Download the dbpedia data into a Azure Blob
# #### Author : spaturu
# #### Date :  07/31/2017

# In[1]:

from azure.storage.blob import BlockBlobService, ContentSettings, PublicAccess, AppendBlobService
#import wget
import requests
import sys
import os
from os import path
from bs4 import BeautifulSoup
import mimetypes
from datetime import datetime
mimetypes.init()
#import urllib

import ckanapi
import json

# In[2]:

#account_name = str(sys.argv[1])
#account_key  = str(sys.argv[2])
#container    = str(sys.argv[3])
#dataset      = str(sys.argv[4])

account_name = str(raw_input ("Enter Azure account name:"))
account_key  = str(raw_input("Enter Azure key:"))
container    = str(raw_input("Enter the container name:"))
dataset      = str(raw_input("enter the Data you want download:"))

block_blob_service = BlockBlobService(account_name = account_name, account_key = account_key)
append_blob_service = AppendBlobService(account_name = account_name, account_key = account_key)


# In[3]:

try:
    if block_blob_service == True:
            print('connection successful!')
except Exception as e:
            print('Please make sure the account name and key are correct.', e)


if block_blob_service.exists(container):
    pass
else:
    block_blob_service.create_container(container)


# In[5]:

# select the dataset based on dataset user input arguement.
urls_dict = {
    'ontology' :['http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.owl',
             'http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.nt'],
     'wikipedia' :['https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-pages-articles-multistream.xml.bz2',
                  'https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-pages-articles-multistream-index.txt.bz2'],
#             'https://creativecommons.org/licenses/by-sa/3.0/legalcode',
 #            'http://www.gnu.org/copyleft/fdl.html'],
#          'datasets' :['http://downloads.dbpedia.org/2016-10/core-i18n/en/'],
         'nlp' :['http://model.dbpedia-spotlight.org/latest_data/en.tar.gz'],
         'dataid':['http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.json',
                   'http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.ttl']
}

urls = urls_dict[dataset]

print urls

# In[6]:
# To upload filedata into Azure fetching directly from URLs
metadata ={}
azure_urls=[]

for url in urls:
    print("URL -->> ", url)
    r = requests.get(url,stream=True)
    file_name = url.split("/")[-1]
    with open(file_name, 'wb') as data:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                data.write(chunk)

    block_blob_service.create_blob_from_path(path.join(container,dataset),
                          data.name,
                          file_name ,
                          content_settings=ContentSettings(content_type=mimetypes.guess_type('./%s' %url.split("/")[-1])[0])
                          )

    print('uploading file to '+''+dataset+' '+'in a '+ container)
    os.remove(data.name)
    download_url = block_blob_service.make_blob_url(path.join(container, dataset),data.name)
    azure_urls.append(download_url)

#metadata[dataset]= azure_urls
metadata['Title'] = 'Dbpedia'+'-'+dataset
metadata
metadata['Publisher'] = 'SiddarthaP'
metadata['Created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
metadata['version'] = "2016-10"
metadata[ "Container"] = container
#metadata['SourceType'] = [url.split(".")[-1] for url in azure_urls]
print("METADATA ====>>> ", metadata)


for azr_url in azure_urls:
 
    metadata[dataset]= azr_url
    metadata['SourceType'] = azr_url.split(".")[-1]
    
    # write the metadata content to file in JSON format
    with open('data.json', 'w') as fp:
        json.dump(metadata, fp)
    
    # to upload Metadata information to CKAN
    APIKEY = "3474fcd0-2ebc-4036-a60a-8bf77eea161f"
    ckan = ckanapi.RemoteCKAN("http://40.71.214.191:80", apikey=APIKEY)
    
    timestmp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = dataset + timestmp
    package_title = dataset + '_metadata_' + timestmp
    try:
        print('Creating "{package_title}" package'.format(**locals()))
        package = ckan.action.package_create(name=package_name, title=package_title, description=azr_url.split("/")[-1])
    except ckanapi.ValidationError as e:
        if (e.error_dict['__type'] == 'Validation Error' and
           e.error_dict['name'] == ['That URL is already in use.']):
            print('"{package_title}" package already exists'.format(**locals()))
            package = ckan.action.package_show(id=package_name)
        else:
            raise
            
    package = ckan.action.package_show(id=package_name)
    
    path = os.path.join('example_files', 'G:\\PC Data\\Software_G\\Ds train\\Ds projects\\data.json')
    r = requests.post('http://40.71.214.191:80/api/action/resource_create',
                      data={'package_id': package['id'],
                            'name': 'metadata',
                          #  'format': 'json',
                            'url': 'upload',  # Needed to pass validation
                            },
                      headers={'Authorization': APIKEY},
                      files=[('upload', file(path))])
    print(r.status_code)
    if r.status_code != 200:
        print('Error while creating resource: {0}'.format(r.content))
        
    
    


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


# In[ ]:



