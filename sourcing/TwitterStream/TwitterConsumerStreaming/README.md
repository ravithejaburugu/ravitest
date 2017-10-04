# Twitter Consumer Streaming
## Overview
This project consumes the 'TwitterHandle' topic from the Kafka broker through Kafka consumer and stores into MongoDB. 

## Instructions

The Dockerfile has the information to build a docker image which in turn is used to build a docker container. Environment variables are defined in .env file and these values can be passed during deployment. 

Below are the list of environment variables to be part of the execution.

* **Agent**

KAFKA_BROKER_URI: The URI of the deployed Kafka broker to connect to (default: localhost:9092)

KAFKA_TOPIC: The Kafka topic the consumer should consume messages from (default: twitterhandle)

* **MongoDB**

REQUIRES_AUTH: Whether or not the MongoDB instance to source into requires authentication (default: false)

MONGO_URI: The URI of the deployed MongoDB instance (default: localhost:27017)

MONGO_USER: If authentication is required, the MongoDB username (default: admin)

MONGO_PASSWORD: If authentication is required, the MongoDB password

MONGO_AUTH_SOURCE: If authentication is required, the database which MongoDB uses as its authentication source (default: admin)

MONGO_AUTH_MECHANISM: If authentication is required, the method which MongoDB uses as its authentication mechanism (default: SCRAM-SHA-1)

MONGO_DB_NAME: The name of the MongoDB database to source into (default: foursquare)

MONGO_COL_NAME: The name of the MongoDB collection within the above database to source into (default: hotels)

MONGO_INDEX_NAME: The field with unique values to create an index on (default: _hash)

## Note:
* Twitter Account handles are included in the config file. For any updates in the Twitter Accounts/Hashtags to be modified at the same location ('HASHTAGS' list in the config.py). To get these changes reflected, Streaming program has to be recompiled and re-run.

Once deployed and run, the script should stream the tweets and data is to be published in MongoDB. 

