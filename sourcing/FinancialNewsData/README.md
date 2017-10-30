# RTIndustryData
## Overview
‘Financial News Extraction’ is the application to fetch the data from various (given 20) web sources in the form of Financial news feeds. Below are the mentioned possible options to perform the extraction.

* 1. RSS feed	: Web source facilitating RSS feed to get the latest news whenever feed is executed.
* 2. Sitemap	: By following the robots exclusion protocol (REP) standards, web sources facilitate to crawl their website using the sitemap URL, available on ‘robots.txt’ for web source.
* 3. API	: API provides the developers to fetch the data from a web source using the classes and methods of the provider by installing their package or using the REST method call.
* 4. Scraping	: When none of the above options are available, we need to manually scrape the tags using beautifulsoup library to crawl each tag and identify actual desired content.

## Instructions


## Requirements:-
* 1. 'Financial Times' subscription and headline API key.
* 2. 'Wall Street Journal' subscription.

Below are the list of arguments to be part of the execution.

* **Agent**
   *	`KAFKA_BROKER_URI`: URI (including host name and port number, if applicable), where Kafka server is running.
   *	`KAFKA_TOPIC_NAME`: A Topic to be used by Kafka Producer to write the message and Kafka Consumer to read from the same.

  *	`REQUIRES_AUTH`: Specify whether the MongoDB Instance needs authentication (default: false)
 *	`MONGO_URI`: The URI of the deployed MongoDB instance (default: localhost:27017)
 *	`MONGO_USER`: Username in case the authentication is specified true.
 *	`MONGO_PASSWORD`: Password in case the authentication is specified true.
 *	`MONGO_AUTH_SOURCE`: If authentication is required, the database which MongoDB uses as its authentication source (default: dbadmin)
 *	`MONGO_AUTH_MECHANISM`: If authentication is required, the method which MongoDB uses as authentication mechanism (default: MONGODB-CR)
 *	`MONGO_DB_NAME`: The name of the MongoDB database to which data is sourced.
 *	`MONGO_COL_NAME`: The name of the MongoDB collection within the database where data is grouped.
 *	`MONGO_INDEX_NAME`: The field with unique values to create an index on.
 *	`MONGO_SSL_REQUIRED`: MongoDB clients can use TLS/SSL to encrypt connections to mongod and mongos instances.

 *	`CKAN HOST`: Account name or the IP address of CKAN Instance.
 *	`CKAN KEY`: Authentication key of the CKAN Instance.
 *	`PUBLISHER`: Name of the person or entity that is publishing the data.

 *	`AUTH_URLS`: Financial Times and WSJ subscription details(email ID and Password).To fetch the whole news article.
 *	`FT_API_KEY`: Financial Times 'HEADLINE API' key.It will fetch all the headlines with news article's urls.

## Note:
* Mongo details need to be exactly same in both folders in config.py, additionally Producer folder will contain 'METADATA' collection name as a constant.

