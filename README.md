# news-analyzer-nikhilgu99

## Homework 2

### Secure File Uploader / Ingestor - Entity Based API

- User Story: A user can securely upload a file of specific formats to be converted into a text file for processing by the *Text NLP Analysis* module.
- Operations: 
    - upload("*filename*") - Upload a file to be converted, will return either a converted text file, or a text file containing an error message (ex: incompatible file type, file too large, bad connection)
    - checkStatus() - Check the status of an uploaded file, will return a string containing the status, which can either be "Success", "Failure - *reason for failure*", or "Progress - *##%*"
- Data: The data handled in this module is the raw file being uploaded, and the text file with the converted file data, which will have the same filename as given, but with the .txt extension


### Text NLP Analysis - Procedure Based API

- User Story: A user can upload a text file and Neural Language Processing (NLP) analysis on it to get certain types of data about it. 
- Operations:
    - upload("*text_file*") - Upload a text file to do NLP analysis on, return string saying if upload is successful and valid, or if an error has occured(invalid filetype, file too large, network error, etc.)
    - getFullAnalysis() - Retrieve all analysis data and return an object containing all data
    - getTranslation("*language*") - Translate file to a specified language, return translated text file
    - getSentiment() - Perform sentiment analysis on file, return a string stating analysis results
    - getRelevantLinks() - Find keywords in the file, and perform a lookup for similar documents online, return an object containing a list of links
- Data: The input data is the text file uploaded by the user. Intermediary data is not seen here as it is handled by the NLP API. Output data depends on the requested analyses, which can either be an object, a text file, or a string


### News Feed Ingestor - Procedure Based API

- User Story: A user can organize a database of new articles URL's, and analyze relations between them to better understand them. In this case the database would be a text file with a single URL per line.
- Operations:
    - addURL("*url*", "*filename*") - Add a URL to a specified file, or create the file if it doesn't exist, return a string with the status of the operation
    - findKeywords(*number*) - Find the top *number* most common keywords amongst the news articles, return a list containing the keywords
    - findNews(*number*, *words[]*, "*filename*") - Find a number of related online news articles to a specific set of keywords, and store their URL's in the given filename, return a string denoting the operations status
    - findSentiment("*filename*") - Gathers an overall sentiment evaluation of all the URL's in a given file, returns a string with the sentiment
    - setSentiment("*sentiment*")- Changes the sentiment to the provided string if the user believes the determined one was incorrect
- Data: The input data would be a text file with one URL per line, where each URL ideally is an identifiable news article. Other handled data here is the sentiment string, and a list containing found common keywords amongst the URL's