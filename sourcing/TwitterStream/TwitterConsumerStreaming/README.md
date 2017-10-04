# Twitter Consumer Streaming
## Overview
This project consumes the specified (default: twitterhandle) topic from the Kafka broker through Kafka consumer and stores into MongoDB. 

## Instructions

The Dockerfile has the information to build a docker image which in turn is used to build a docker container. Environment variables are defined in .env file and these values can be passed during deployment. 

Below are the list of environment variables to be part of the execution.

* **Agent**

    * `KAFKA_BROKER_URI`: The URI of the deployed Kafka broker to connect to (default: localhost:9092)

    * `KAFKA_TOPI`: The Kafka topic the consumer should consume messages from (default: twitterhandle)

* **MongoDB**

    * `REQUIRES_AUTH`: If the MongoDB instance to source into requires authentication (default: `false`)
    
    * `MONGO_URI`: The URI of the deployed MongoDB instance (default: `localhost:27017`)
    
    * `MONGO_USER`: If authentication is required, the MongoDB username
    
    * `MONGO_PASSWORD`: If authentication is required, the MongoDB password
    
    * `MONGO_AUTH_SOURCE`: If authentication is required, the database which MongoDB uses as its authentication source (default: `dbadmin`)
    
    * `MONGO_AUTH_MECHANISM`: If authentication is required, the method which 
    MongoDB uses as its authentication mechanism (default: `MONGODB-CR`)
    
    * `MONGO_DB_NAME`: The name of the MongoDB database to source into 
    
    * `MONGO_COL_NAME`: The name of the MongoDB collection within the above database to 
    source into
    
    * `MONGO_INDEX_NAME`: The field with unique values to create an index on


## Note:

Once deployed and run, the script should consume messages from the broker and publish to MongoDB. 

