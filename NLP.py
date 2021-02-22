# Text NLP Analysis

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting a filetype or a large/invalid number.
# Errors can show up when there are network errors, file handling errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

class fullNLP:
    def __init__(self, sentiment, links):
        self.sentiment = sentiment # String with NLP determined sentiment
        self.relevantLinks = links # List of determined relevant links, default to 5?


# Functions

def uploadNLP(filename):
    logging.info("User has successfully uploaded a text file for NLP analysis")

    return("File successfully uploaded for NLP analysis.")

def getFullAnalysis():
    logging.info("User has done full NLP analysis")
    
    retVal = fullNLP("call sentiment function here", ["call link", "function here"])
    return retVal

def getTranslation(language):
    logging.info("User has translated text file")

    return("Translation successful")

def getSentiment():
    logging.info("User has gotten sentiment of text file")

    return("Positive")

def getRelevantLinks(number):
    logging.info("User has gotten links related to text file")

    return("Successfully found and saved links")