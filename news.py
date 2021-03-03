# News Feed Ingestor

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting a invalid data types.
# Errors can show up when there are network errors, Public API errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

# Functions

def queryKeywords(words): # Get a list of articles related to a list of keywords
    logging.info("User has queried for articles using keywords")

    return ("Article 1 URL | Article 2 URL | Article 3 URL")

def queryPerson(name): # Get a list of articles related to a person's name
    logging.info("User has queried using a name")

    return("Article 1 URL | Article 2 URL | Article 3 URL")

def queryHistorical(year, month, words): # Get a list of articles related to a list of keywords, during a specific month & year
    logging.info("User has queried using for historical arcticles")

    return("Article 1 URL | Article 2 URL | Article 3 URL")

