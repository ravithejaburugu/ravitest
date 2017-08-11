# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 11:00:16 2017

@author: Admin
"""

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
from config import argument_config

def assignAzureContainer(block_blob_service, container):
    # To check the connection is established sucessfully.
    try:
        if block_blob_service == True:
                print('Connection successful!')
    except Exception as e:
                print('Please make sure the account name and key are correct.', e)
    
    # If container already exists with the given name in azure, it will create a new container     
    if not block_blob_service.exists(container):
        block_blob_service.create_container(container)

archive_url = "http://downloads.dbpedia.org/2016-10/core-i18n/en/"
def get_links():
     
    # create response object
    r = requests.get(archive_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content)
     
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
         'wikipedia' :[
		       'https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-stub-meta-history26.xml.gz',
                       'http://downloads.dbpedia.org/2016-10/core-i18n/en/pages_articles_en.xml.bz2'
                       ],
         'datasets' :data_links,
         'nlp' :['http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/genders_en.nt.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/lexicalizations_en.nq.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/topic_signatures_en.tsv.bz2',
                     'http://wifo5-04.informatik.uni-mannheim.de/downloads/datasets/topical_concepts.nt.bz2'],
         'dataid':['http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.json',
                       'http://downloads.dbpedia.org/2016-10/2016-10_dataid_catalog.ttl'],
	 'license':['https://creativecommons.org/licenses/by-sa/3.0/legalcode',
                       'http://www.gnu.org/copyleft/fdl.html']
    }
    #urls = urls_dict[dataset] + urls_dict['license']
    urls = urls_dict[dataset]
    return urls



# To upload filedata into Azure fetching directly from URLs
def downloadToAzure(urls, block_blob_service, container, dataset, ds_type):
    metadata ={}
    azure_urls=[]

    for url in urls:
        #print("Dataset URL -->> ", url)
        file_name = url.split("/")[-1]  
        #print("file_name-> "+file_name)
            
        # if 'license' in url or 'html' in url:
        if ds_type == 'license':
            r = requests.get(url,stream=True)
            stream = io.BytesIO(r.content)
            #file_name = url.split("/")[-1]
            block_blob_service.create_blob_from_stream(path.join(container, dataset),
                              file_name, stream, max_connections=2,
                              content_settings=ContentSettings(content_type=mimetypes.guess_type('./%s' %file_name)[0]))
        else :
            #print('copying blob')
            block_blob_service.copy_blob(path.join(container, dataset), file_name, url)
        
        #print("Downloading '"+file_name+"' to '"+dataset+"' folder in Azure container '"+ container +"'")
        download_url = block_blob_service.make_blob_url(path.join(container, dataset), file_name)
        azure_urls.append(download_url)

    if ds_type == 'dataset':
        print("Total " + str(len(azure_urls)) + " files downloaded")
    
    # Creating metadata of the uploaded dataset files, not for license 
    if ds_type == 'dataset':
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


# Function executes for 'datasets', as artifacts are to be created for all 166 urls 
def uploadMultipleArtifactsToCKAN(azure_urls, metadata, dataset, ckan_host, api_key):
    urls= ''
    artifact_old=''
    urls_new=''
    
    
    for azr_url in azure_urls:
        
        if(len(urls)>1):
            urls+= ', '
        urls+= azr_url
        
            
        print(azr_url)
        
        file_name = azr_url.split("/")[-1].split(".")[0]
        artifact=''
        artifact = file_name[0:file_name.index('_en')].replace("_", " ")
         
        if(artifact==artifact_old):
            urls_new+=urls
        print("datasets's dataset artifact --> " + artifact)
        
        if((artifact != artifact_old) and (artifact_old != '')):
            
            uploadMetaDataToCKAN([urls_new], metadata, dataset, ckan_host, api_key, artifact)
            urls_new= ''
            urls= ''
            
            
            
        
        artifact_old=artifact


# Upload all the metadata details into CKAN
def uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, artifact):
   urls = ''
   sourceTypes = ''
   #print(azure_urls)
   
   for azr_url in azure_urls:
       if(len(urls)>1):
           urls += ', '
       urls += azr_url
    
       srctyp = ''
       url_ext = azr_url.split("/")[-1]
       
       if(url_ext.split(".")[-1] == 'bz2' or url_ext.split(".")[-1] == 'gz'):
           srctyp += url_ext.split(".")[-2:-1][0]
       else:
           srctyp += url_ext.split(".")[-1]        
           
       if srctyp not in sourceTypes:
           if(len(sourceTypes)>1):
               sourceTypes += ', '
           sourceTypes += srctyp
               
   #print("Azure URLs -> ")
   #print(urls)
   #print("Source types -> ")
   #print(sourceTypes)

   metadata['URL']= urls
   metadata['SourceType'] = sourceTypes
       
   # write the metadata content to file in JSON format
   with open(dataset+'_data.json', 'w') as fp:
       json.dump(metadata, fp)

   print("METADATA --> ", metadata)

   # Connecting to CKAN
   ckan_ckan = ckanapi.RemoteCKAN(ckan_host, apikey=api_key)
   
   with open('data.json') as data_file:
       jsondata = json.load(data_file)

   path = os.path.join(os.path.dirname(__file__), dataset+'_data.json')
   #file_data = file(path)

   #timestmp = datetime.now().strftime("%Y%m%d_%H%M%S")
   #time_only = datetime.now().strftime("%H%M%S")

   package_name = artifact.replace(' ', '_').lower() #+ timestmp
   dataset = artifact
   artifact_json = jsondata["metadata"][dataset]

   if str(artifact_json) :
       package_title = artifact_json["Title"] #+ '_' + time_only
    
       try:
           print('Creating "{package_title}" package in CKAN'.format(**locals()))
           package = ckan_ckan.action.package_create(name=package_name, title=package_title,
                              notes=artifact_json["Description"],
                              maintainer=artifact_json["Publisher"],
                              version=artifact_json["version"],
                              license_id=artifact_json["License"],
                              tags=[{'name':tag} for tag in artifact_json["Tags"].split(',')]
                              #resorces=azure_urls
                              )
       except ckanapi.ValidationError as e:
           if (e.error_dict['__type'] == 'Validation Error' and
              e.error_dict['name'] == ['That URL is already in use.']):
               print('"{package_title}" package already exists'.format(**locals()))
               package = ckan_ckan.action.package_update(id=package_name, title=package_title,
                              notes=artifact_json["Description"],
                              maintainer=artifact_json["Publisher"],
                              version=artifact_json["version"],
                              license_id=artifact_json["License"],
                              tags=[{'name':tag} for tag in artifact_json["Tags"].split(',')]
                              )
           else:
               raise
    
       package = ckan_ckan.action.package_show(id=package_name)
    
       r = requests.post(ckan_host+'/api/action/resource_create',
                         data= {'Title':artifact_json["Title"],
                                 'package_id': package['id'],
                                 'name': artifact_json["Title"],
                                 'Azure URL':urls,
                                 'Source':artifact_json["Source"],
                                 'Source type':sourceTypes, #artifact_json["Source_type"],
                                 #'Description':artifact_json["Description"],
                                 #'version':artifact_json["version"],
                                 #'Author':artifact_json["Publisher"],
                                 #'License':artifact_json["License"],
                                 'url': 'upload'  # Needed to pass validation
                               },
                         headers={'Authorization': api_key},
                         files=[('upload', file(path))])
       print(r.status_code)
       if r.status_code != 200:
           print('Error while creating resource: {0}'.format(r.content))
       print("-- Data is now available in Azure and Metadata in CKAN --")
   
        
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
    account_name = argument_config.get('azure_account_name')#str(sys.argv[1])
    account_key  = argument_config.get('azure_account_key')#str(sys.argv[2])
    container    = argument_config.get('container')
    dataset      = argument_config.get('dataset')
    ckan_host    = argument_config.get('ckan_host')
    api_key      = argument_config.get('ckan_key')

    #print(len(sys.argv))
    
   
    
    #print(account_name, account_key, container, dataset)
    
    # Azure blob services used to access azure
    block_blob_service = BlockBlobService(account_name = account_name, account_key = account_key)
    #append_blob_service = AppendBlobService(account_name = account_name, account_key = account_key)
    
    assignAzureContainer(block_blob_service, container)
    
    # begin copying license in the azure container
    urls = fetchUrls('license')
    downloadToAzure(urls, block_blob_service, container, dataset, 'license')
    
    # download the dataset to the azure container
    urls = fetchUrls(dataset)
    metadata, azure_urls = downloadToAzure(urls, block_blob_service, container, dataset, 'dataset')
    
    # upload metadata into CKAN
    if dataset == 'datasets':
        uploadMultipleArtifactsToCKAN(azure_urls, metadata, dataset, ckan_host, api_key)
    else:
        uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, dataset)
    

    
if __name__ == "__main__":
    main()