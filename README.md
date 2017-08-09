# DBPedia Data
## Overview
The above code sources all the Dbpedia content and stores it into a Azure blob inside a container. Once the data is loaded, the metadata about each of the artifact will be stored to CKAN Data management system. The metadata is available under metadata.json file which can be modified as needed before deploying the script.

## Instructions
The Dockerfile has the information to build a docker image which in turn is used to build a docker container. The above python script accepts six arguments namely Azure host, Azure Key, Azure container, Dataset group (wikipedia, ontology, dataset, nlp, dataid and license), CKAN host and CKAN API key.
When deploying script, the command should be entered as below.

`Docker run {image} python dbPedia.py {Azure host} {Azure key} {Azure container} {Dataset group} {CKAN host} {CKAN key}`

Once run, the script should load the data into Azure and CKAN storage. Please verify to make sure the data is loaded. 

* Note: Some of the larger dump files may take longer to load 

