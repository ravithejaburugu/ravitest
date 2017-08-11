# DBpedia Data
## Overview
This project sources all the DBpedia content and stores it into a Azure blob inside a container. Once the data is loaded, the metadata about each of the artifact will be stored to CKAN Data management system. The metadata is available under data.json file which can be modified as needed before deploying the script.

## Instructions
The Dockerfile has the information to build a docker image which in turn is used to build a docker container. Environment variables are defined in .env file and these values can be passed during execution time. The script accepts six variables namely Azure host, Azure Key, Azure container, Dataset group (wikipedia, ontology, datasets, nlp and dataid), CKAN host and CKAN API key.

Once deployed and run, the script should load the data into Azure and CKAN storage. Please verify to make sure the data is published. 

* Note: Some of the larger dump files may take longer to load 

