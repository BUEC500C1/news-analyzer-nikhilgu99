# news-analyzer-nikhilgu99

## Homework 2

## NOTE: For results/testing update due 4/1/2021, refer to RESULTS.md

### Secure File Uploader / Ingestor - Entity Based API

- User Story: A user can securely upload a PDF file to be converted into a text file for processing by the *Text NLP Analysis* module.
- Operations: 
    - upload("*filename*") - Upload a file to be converted, will return a message indicating status
    - read("*file_id*") - Retrieve a text file for viewing, will return a message indicating status, and print text to GUI
    - update("*file_id*","*id*","*value*") - Update the attributes / metadata of an uploaded file, will return a string indicating the status of the operation
    - delete("*file_id*") - Delete a file from the database, will return the status of the operation


### Text NLP Analysis - Procedure Based API

- User Story: A user can upload text and run Neural Language Processing (NLP) analysis on it to get certain types of information about the text. I chose the IBM Watson Cloud NLP API.
- Operations:
    - getEntities("*text*") - Perform entity analysis on text, return a string stating analysis results
    - getSentiment("*text*") - Perform sentiment analysis on text, return a string stating analysis results
    - getEntitySentiment("*text*") - Perform both entity and sentiment analysis on text, return a string stating analysis results
    - getClassification("*text*") - Perform content classification by topic, return a string stating analysis results


### News Feed Ingestor - Procedure Based API

- User Story: A user can search a database of news articles. In this case the database would be connected to the New York Times API. Queries can be done based on keywords, people, and historically. A maximum of 10 results will be returned, sorted by most recent.
- Operations:
    - queryKeyword(*keyword*) - Return a list of articles related to a given keyword
    - queryPerson("*name*") - Return a list of articles related to a given person's name
    - queryHistorical(*keyword*, *startDate*, *endDate*) - Return a list of articles during a certain time period, related to a given keyword


### Database Configuration

This API uses the SQLite3 library. I have a table called "files" to store information about pdf and text files uploaded by the file upload API. The columns in this table are file ID, filename, upload date, and data.