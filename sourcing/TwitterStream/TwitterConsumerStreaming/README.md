# Twitter Consumer Streaming
## Overview
This project consumes the 'TwitterHandle' topic from the Kafka broker through Kafka consumer and stores into MongoDB. 

## Instructions

The Dockerfile has the information to build a docker image which in turn is used to build a docker container. Environment variables are defined in .env file and these values can be passed during deployment. 

Below are the list of arguments to be part of the execution.

* 'CONSUMER_KEY': Twitter consumer key to recognise the source.
* 'CONSUMER_SECRET': Twitter consumer secret authenticates the source application user.
* 'ACCESS_TOKEN': Twitter access token replaces the user access for OAuth.
* 'ACCESS_TOKEN_SECRET': Twitter access token secret authenticates without password, using OAuth.
* 'KAFKA_BROKER_URI': URI (including host name and port number, if applicable), where Kafka server is running.
* 'KAFKA_TOPIC_NAME': A Topic to be used by Kafka Producer to write the message and Kafka Consumer to read from the same.

## Note:
* Twitter Account handles are included in the config file. For any updates in the Twitter Accounts/Hashtags to be modified at the same location ('HASHTAGS' list in the config.py). To get these changes reflected, Streaming program has to be recompiled and re-run.

Once deployed and run, the script should stream the tweets and data is to be published in MongoDB. 

