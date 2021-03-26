# Text NLP Analysis

import json
import logging

# IBM NLP API Imports
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, EntitiesOptions, SentimentOptions

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting large text or invalid characters.
# Errors can show up when there are network errors, Public NLP API errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

authenticator = IAMAuthenticator('edJ96pfFUB2JT949IVN-aLuGIrAs75NLpfHfbw5sBB18')
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2020-08-01', authenticator=authenticator)
natural_language_understanding.set_service_url('https://api.us-east.natural-language-understanding.watson.cloud.ibm.com/instances/3528455f-6fa6-4e10-8eb8-1e0cdf7779e0')

# Functions

def getEntities(inp): # Perform entity analysis on a text (names, nouns, places, etc.)
    logging.info("User has gotten entities found in text")

    response = natural_language_understanding.analyze(text=inp,features=Features(entities=EntitiesOptions(sentiment=True,limit=10))).get_result()

    if response['entities'] == []:
        logging.info("No entities found for given text.")
        return "No entites found for the given text."

    entities = ""
    for entity in response['entities']:
        entities += (entity['text'] + " - " + entity['type'] + "<br>")

    return entities

def getSentiment(inp): # Perform sentiment analysis on a text (Positive, Neutral, Negative)
    logging.info("User has gotten sentiment of text")

    response = natural_language_understanding.analyze(text=inp,features=Features(sentiment=SentimentOptions())).get_result()

    return (response['sentiment']['document']['label'] + ": " + str(response['sentiment']['document']['score']))

def getEntitySentiment(inp): # Perform both sentiment and entity analysis on a text
    logging.info("User has gotten entities and sentiment of text")

    retVal = "<h4>ENTITY ANALYSIS</h4><br>"

    # ENTITY ANALYSIS
    entityResponse = natural_language_understanding.analyze(text=inp,features=Features(entities=EntitiesOptions(sentiment=True,limit=10))).get_result()

    if entityResponse['entities'] == []:
        logging.info("No entities found for given text.")
        retVal += "No entites found for the given text.<br>"
    else:
        for entity in entityResponse['entities']:
            retVal += (entity['text'] + " - " + entity['type'] + "<br>")

    retVal += "<br><h4>SENTIMENT ANALYSIS</h4><br>"

    # SENTIMENT ANALYSIS
    sentimentResponse = natural_language_understanding.analyze(text=inp,features=Features(sentiment=SentimentOptions())).get_result()
    retVal += (sentimentResponse['sentiment']['document']['label'] + ": " + str(sentimentResponse['sentiment']['document']['score']))

    return retVal

def getClassification(inp): # Classify a text into a general topic / field
    logging.info("User has classified text by topic.")

    response = natural_language_understanding.analyze(text=inp,features=Features(categories=CategoriesOptions(limit=3))).get_result()

    categories = ""
    for category in response['categories']:
        categories += (category['label'] + " - " + str(category['score']) + "<br>")

    return categories