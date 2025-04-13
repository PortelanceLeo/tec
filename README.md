# tec_interview
tec_interview instructions

Objective:

The objective of this project is to create a software project which when launched will download CSVs from the internet, parse and validate the data contained in the CSVs and then insert it into a relational database.

The CSVs describe the shipment of natural gas. There are CSVs published multiple times a day (each day is divided into cycles). When launched the program should download, parse and insert the data available from the last three days.

Deliverables:

- DDL of a database table(s) where the data will be inserted. (Postgres SQL preferred, but any relational DB is okay)

- The necessary query(s) to insert this data.

- The code to facilitate the downloading, validation, and insertion of the data. C# and Python are our preferred languages but feel free to use something else if you would feel more comfortable.

- Instructions on how to run the code in the form of a readme.

The deliverables should all be uploaded to a public git repository (like GitHub)

The site where the data is found:
https://twtransfer.energytransfer.com/ipost/TW/capacity/operationally-available

An example url that can be used to download the CSV over HTTP:
https://twtransfer.energytransfer.com/ipost/capacity/operationally-available?f=csv&extension=csv&asset=TW&gasDay=01%2F18%2F2024&cycle=3&searchType=NOM&searchString=&locType=ALL&locZone=ALL


## Command to run stuff
PG_USER=leo PG_PASSWORD=verysafe42 DB=test_db ./run.sh


