"""
Created on Mon Aug 07 18:13:49 2017

@author: Admin
"""


# coding: utf-8

# #### Name : Download the dbpedia data into a Azure Blob
# #### Author : spaturu
# #### Date :  07/31/2017

# In[1]:

from azure.storage.blob import BlockBlobService, ContentSettings, PublicAccess, AppendBlobService
import wget
import requests
import sys
import os
from os import path
from bs4 import BeautifulSoup
import mimetypes
from datetime import datetime
mimetypes.init()
import urllib
import ckanapi
import json
import io
from pprint import pprint
from tqdm import tqdm

def assignAzureContainer(block_blob_service, container):
    try:
        if block_blob_service == True:
                print('Connection successful!')
    except Exception as e:
                print('Please make sure the account name and key are correct.', e)
        
    if block_blob_service.exists(container):
        pass
    else:
        block_blob_service.create_container(container)

archive_url = "http://downloads.dbpedia.org/2016-10/core-i18n/en/"
def get_links():
     
    # create response object
    r = requests.get(archive_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content,'lxml')
     
    # find all links on web-page
    links = soup.findAll('a')
 
    # filter the link sending with .bz2
    data_links = [archive_url + link['href'] for link in links if link['href'].endswith('bz2')]
 
    return data_links
data_links = get_links()


# select the dataset based on dataset user input arguement.
# for testing purpose, only limited URLs are provided.
def fetchUrls(dataset):    
    urls_dict = {
         'ontology' :['http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.owl',
                      'http://downloads.dbpedia.org/2016-10/dbpedia_2016-10.nt'],
         'wikipedia' :['https://creativecommons.org/licenses/by-sa/3.0/legalcode',
                       'http://www.gnu.org/copyleft/fdl.html',
		       'https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-stub-meta-history26.xml.gz'
                       'http://downloads.dbpedia.org/2016-10/core-i18n/en/pages_articles_en.xml.bz2',
                       ],
              'datasets' :data_links,
         'nlp' :['http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/genders_en.nt.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/lexicalizations_en.nq.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/topic_signatures_en.tsv.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/topical_concepts.nt.bz2'],
         'dataid':['http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.json',
                       'http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.ttl']
    }
    urls = urls_dict[dataset]
    return urls



# To upload filedata into Azure fetching directly from URLs
def downloadToAzure(urls, block_blob_service, container,dataset):
    metadata ={}
    azure_urls=[]
        
    for url in urls:
        print("Dataset URL -->> ", url)
        file_name = url.split("/")[-1]  
        block_blob_service.copy_blob(path.join(container,dataset),file_name,url)
        print('Uploading file to "'+dataset+'" '+'in Azure container "'+ container +'"')
	download_url = block_blob_service.make_blob_url(path.join(container, dataset),data.name)
        azure_urls.append(download_url)

    # Creating metadata of the uploaded files 
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata['Title'] = 'Dbpedia'+'-'+dataset
    metadata['Description'] = 'Dummy description for testing.'
    metadata['Publisher'] = 'RandomTrees'
    metadata['Created'] = current_date
    metadata['Last Updated'] = current_date
    metadata['Sourcing_Date'] = current_date
    metadata['version'] = "2016-10"
    metadata['Container'] = container
    #metadata['SourceType'] = [url.split(".")[-1] for url in azure_urls]
    metadata['License'] = "Creative Common Attribution, GNU Free Documentation Licsensing."

    return metadata, azure_urls


# Upload all the metadata details into CKAN
def uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key):
    for azr_url in azure_urls:

        metadata['URL']= azr_url
        metadata['SourceType'] = azr_url.split(".")[-1]
        
        # write the metadata content to file in JSON format
        with open(dataset+'data.json', 'w') as fp:
            json.dump(metadata, fp)

        print("METADATA ===>> ", metadata)

        # Connecting to CKAN
        ckan_ckan = ckanapi.RemoteCKAN(ckan_host, apikey=api_key)
        
        with open('data.json') as data_file:
            jsondata = json.load(data_file)
        
        timestmp = datetime.now().strftime("%Y%m%d_%H%M%S")
        package_name = dataset + timestmp
        package_title = jsondata["metadata"][dataset]["Title"] + '_Metadata_' + timestmp
        
        try:
            print('Creating "{package_title}" package in CKAN'.format(**locals()))
            package = ckan_ckan.action.package_create(name=package_name, title=package_title, 
                               description=azr_url.split("/")[-1])
            #package = ckan.logic.action.package_create(True, metadata)
        except ckanapi.ValidationError as e:
            if (e.error_dict['__type'] == 'Validation Error' and
               e.error_dict['name'] == ['That URL is already in use.']):
                print('"{package_title}" package already exists'.format(**locals()))
                package = ckan_ckan.action.package_show(id=package_name)
            else:
                raise
                
        package = ckan_ckan.action.package_show(id=package_name)

        path = os.path.join(os.path.dirname(__file__), dataset+'data.json')
        file_data = file(path)
                            
        r = requests.post(ckan_host+'/api/action/resource_create',
                          data= {'Title':jsondata["metadata"][dataset]["Title"],
                                  'Description':jsondata["metadata"][dataset]["Description"],
                                  'version':jsondata["metadata"][dataset]["version"],
                                  'Author':jsondata["metadata"][dataset]["Publisher"],
                                  'package_id': package['id'],
                                  'name': jsondata["metadata"][dataset]["Title"] + '_metadata_' + timestmp,
                                  'Azure URL':azr_url,
                                  'Source':jsondata["metadata"][dataset]["Source"],
                                  'Source type':jsondata["metadata"][dataset]["Source_type"],
                                  'License':jsondata["metadata"][dataset]["License"],
                                  'url': 'upload'  # Needed to pass validation
                                },
                          headers={'Authorization': api_key},
                          files=[('upload', file(path))])
        print(r.status_code)
        if r.status_code != 200:
            print('Error while creating resource: {0}'.format(r.content))
        print("-- Data is now available in Azure and Metadata in CKAN --")

            
        
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

def download_data(data_links):
     for link in data_links:
         
         '''iterate through all links in data_links
         and download them one by one'''
          
         # obtain filename by splitting url and getting last string
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


	 
def main():
    # Collect the user input arguements
    account_name = str(sys.argv[1])
    account_key  = str(sys.argv[2])
    container    = str(sys.argv[3])
    dataset      = str(sys.argv[4])
    
    ckan_host = ''
    api_key = ''

    #print(len(sys.argv))
    
    if len(sys.argv) > 5:
        ckan_host = str(sys.argv[5])
        api_key = str(sys.argv[6])
    else:
        ckan_host = "http://40.71.214.191:80"
        api_key = "3474fcd0-2ebc-4036-a60a-8bf77eea161f"
    
    print(account_name, account_key, container, dataset)
    
    # Azure blob services used to access azure
    block_blob_service = BlockBlobService(account_name = account_name, account_key = account_key)
    append_blob_service = AppendBlobService(account_name = account_name, account_key = account_key)
    
    assignAzureContainer(block_blob_service, container)
    
    urls = fetchUrls(dataset)
    
    metadata, azure_urls = downloadToAzure(urls, block_blob_service, container,dataset)
    
    uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key)
    
#    data_links = get_links()
#    print(data_links)

#    download_data(data_links)

    
if __name__ == "__main__":
    main()
    

    
