## Quandl

Financial Data

To fetch Financial data both persisted and live data, we can use the provided URLs or Quandl codes along with the registered API Key. Data has to be fetched from about 195 datasets (when this document is made).
REST API request URLs of the data sources can be passed using a CSV file.
Quandl API also can be used to get data dump for every request made using Quandl code.
API Key: It can be generated at Quandl upon creating an account at https://www.quandl.com/

Data Fetching
Quandl provides 2 types of APIs:
1.	Time-series
https://www.quandl.com/api/v3/datasets/{database_code}/{dataset_code}/data.{return_format} 
2.	Tables
https://www.quandl.com/api/v3/datatables/{datatable_code}.{format}?<row_filter_criteria> 
JSON Response format is preferred over CSV and XML as it is suitable for MongoDB storage.
More details are available at the documentation page https://docs.quandl.com/docs

Data Storing
Each collection is maintained for every dataset in the MongoDB. A Metadata collection helps maintain a record of what all datasets have been downloaded.
The MongoDB host URI can be maintained in the CKAN. Last updated time helps in identifying when the program was executed latest.
