# News Feed Ingestor

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting a filetype or a large/invalid number.
# Errors can show up when there are network errors, file handling errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

# Functions

def addURL(url, filename):
    logging.info("User has added a URL to a file")

    return("Successfully added URL")

def findKeywords(number):
    logging.info("User has queried for common keywords")

    return ["word1", "word2"]

def findNews(number, words, filename):
    logging.info("User has queried for related news stories")

    return("Successfully found and added news")

def findSentiment(filename):
    logging.info("User has found overall sentiment of stories")

    return("Determined Sentiment: Positive")

