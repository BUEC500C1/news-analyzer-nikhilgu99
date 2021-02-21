# Text NLP Analysis

# Data

class fullNLP:
    def __init__(self, sentiment, links):
        self.sentiment = sentiment # String with NLP determined sentiment
        self.relevantLinks = links # List of determined relevant links, default to 5?


# Functions

def uploadNLP(filename):

    return("File successfully uploaded for NLP analysis.")

def getFullAnalysis():
    
    retVal = fullNLP("call sentiment function here", ["call link", "function here"])
    return retVal

def getTranslation(language):

    return("Translation successful")

def getSentiment():

    return("Positive")

def getRelevantLinks(number):

    return("Successfully found and saved links")