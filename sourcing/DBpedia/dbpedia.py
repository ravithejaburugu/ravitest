# coding: utf-8

# #### Name : Download the dbpedia data into a Azure Blob
# #### Author : spaturu
# #### Date :  07/31/2017

# In[1]:

from azure.storage.blob import BlockBlobService, ContentSettings, PublicAccess, AppendBlobService
import requests
import sys
import os
from os import path
from bs4 import BeautifulSoup
import mimetypes
from datetime import datetime
mimetypes.init()
import ckanapi
import json
import io
from pprint import pprint
from tqdm import tqdm
from config import argument_config


# Creating Azure container
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
# fetch list of urls from a web page
def get_links():
     
    # create response object
    r = requests.get(archive_url)
     
    # create beautiful-soup object
    soup = BeautifulSoup(r.content, "html.parser")
     
    # find all links on web-page
    links = soup.findAll('a')
 
    # filter the link sending with .bz2
    data_links = [archive_url + link['href'] for link in links if link['href'].endswith('bz2')]
 
    return data_links
data_links = get_links()


# select the dataset based on user input arguement.
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


# To upload filedata into Azure container, fetching directly from URLs
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

    #if ds_type == 'dataset':
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


# Function executes for 'datasets', as artifacts are to be created for all the bulk of URLs 
def uploadMultipleArtifactsToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, owner_org):
    artifacts = []
    common_urls = []
    artif_urls_dict = {}

    # fetch the appropriate artifact name based on the filename part of the URL.    
    for azr_url in azure_urls:        
        file_name = azr_url.split("/")[-1].split(".")[0]
        artifact = file_name[0:file_name.index('_en')].replace("_", " ")
        artifacts.append(artifact)
        #print("datasets's artifact --> " + artifact)
        
        # Club the URLs related to same artifact.
        if artifact in artif_urls_dict:
            common_urls = artif_urls_dict[artifact]
            common_urls.append(azr_url)
        else:
            common_urls = [azr_url]
        
        artif_urls_dict[artifact] = common_urls
            
    # loop to create package for each artifact in CKAN
    for artif in artif_urls_dict:
        uploadMetaDataToCKAN(artif_urls_dict[artif], metadata, dataset, ckan_host, api_key, owner_org, artif)


# Upload all the metadata details into CKAN
def uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, owner_org, artifact):
   urls = ''
   sourceTypes = ''
   
   # fetch source types of the files from the URLs 
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
               
   metadata['URL']= urls
   metadata['SourceType'] = sourceTypes
       
   print(urls)
   
   # write the metadata content to file in JSON format
   with open(dataset+'_data.json', 'w') as fp:
       json.dump(metadata, fp)

   # Connecting to CKAN
   ckan_ckan = ckanapi.RemoteCKAN(ckan_host, apikey=api_key)
   
   # pull the static content from "data.json" file
   with open('data.json') as data_file:
       jsondata = json.load(data_file)

   path = os.path.join(os.path.dirname(__file__), dataset+'_data.json')

   package_name = artifact.replace(' ', '_').lower()
   dataset = artifact
   artifact_json = jsondata["metadata"][dataset]

   # create or update the package for each artifact with latest Metadata of Azure datasets.
   if str(artifact_json) :
       package_title = artifact_json["Title"].replace('.','')       
       tags = [{'name': str(tag).strip()} for tag in artifact_json["Tags"].split(',')]
       try:
           package = ckan_ckan.action.package_show(id=package_name)
           if package:
               package = ckan_ckan.action.package_update(id=package_name, 
                                  title=package_title,
                                  notes=artifact_json["Description"],
                                  maintainer=artifact_json["Publisher"],
                                  version=artifact_json["version"],
                                  license_id=artifact_json["License"],
                                  tags=tags 
                                  )
           else:
               package = ckan_ckan.action.package_create(name=package_name, 
                                  title=package_title,
                                  notes=artifact_json["Description"],
                                  maintainer=artifact_json["Publisher"],
                                  version=artifact_json["version"],
                                  license_id=artifact_json["License"],
                                  tags=tags 
                                  )
           
           r = requests.post(ckan_host+'/api/action/resource_create',
                             data= {'Title':package_title,
                                     'package_id': package['id'],
                                     'name': package_title,
                                     'Azure URL':urls,
                                     'Source':artifact_json["Source"],
                                     'Source type':sourceTypes, 
                                     'owner_org':owner_org,
                                     'url': 'upload'  # Needed to pass validation
                                   },
                             headers={'Authorization': api_key},
                             files=[('upload', file(path))])
           print(r.status_code)
           if r.status_code != 200:
               print('Error while creating resource: {0}'.format(r.content))
           else:
               print('Created "{package_title}" package in CKAN'.format(**locals()))       
       except:
           raise

        
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
    owner_org    = argument_config.get('owner_org')
    
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
        uploadMultipleArtifactsToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, owner_org)
    else:
        uploadMetaDataToCKAN(azure_urls, metadata, dataset, ckan_host, api_key, owner_org, dataset)
    

    
if __name__ == "__main__":
    main()
    

    
