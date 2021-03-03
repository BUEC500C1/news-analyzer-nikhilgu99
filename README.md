# news-analyzer-nikhilgu99

## Homework 2

### Secure File Uploader / Ingestor - Entity Based API

- User Story: A user can securely upload a PDF file to be converted into a text file for processing by the *Text NLP Analysis* module.
- Operations: 
    - upload("*filename*") - Upload a file to be converted, will return a message indicating status
    - read("*filename*") - Retrieve a text file for viewing, will return a message indicating status, and print text to GUI (?)
    - update("*filename*","*id*","*value*") - Update the attributes / metadata of a text file, will return a string indicating the status of the operation
    - delete("*filename*") - Delete a file from the database, will return the status of the operation


### Text NLP Analysis - Procedure Based API

- User Story: A user can upload text and run Neural Language Processing (NLP) analysis on it to get certain types of information about the text. (Current stub based off of Google NLP API)
- Operations:
    - getSentiment("*text*") - Perform sentiment analysis on text, return a string stating analysis results
    - getEntities("*text*") - Perform entity analysis on text, return a string stating analysis results
    - getEntitySentiment("*text*") - Perform both entity and sentiment analysis on text, return a string stating analysis results
    - getClassification("*text*") - Perform content classification by topic, return a string stating analysis results


### News Feed Ingestor - Procedure Based API

- User Story: A user can search a database of news articles, and analyze relations between them to better understand them. In this case the database would be conncted to some public news API.
- Operations:
    - queryKeywords(*words[]*) - Return a list of articles related to a list of given keywords
    - queryPerson("*name*") - Return a list of articles related to a given person's name
    - queryHistorical(*year*, *month*, *words[]*) - Return a list of articles during a certain month/year, related to a given list of words