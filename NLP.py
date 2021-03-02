# Text NLP Analysis

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting large text or invalid characters.
# Errors can show up when there are network errors, Public NLP API errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

# Functions

def getSentiment(text):
    logging.info("User has gotten sentiment of text")

    return("Score: 0.9 (Positive)")

def getEntities(text):
    logging.info("User has gotten entities found in text")

    return("Found xyz names, xyz nouns, xyz place.")

def getEntitySentiment(text):
    logging.info("User has gotten sentiment and entities of text")

    return("Score: 0.9 (Positive)- Found xyz names, xyz nouns.")

def getClassification(text):
    logging.info("User has classified text by topic.")

    return("Topic: Computer Science - Confidence: 0.9")