# News Feed Ingestor

import json
import logging

from urllib.request import urlopen

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting a invalid data types.
# Errors can show up when there are network errors, Public API errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Functions

def queryKeyword(keyword): # Get a list of articles related to a list of keywords
    logging.info("User has queried for articles using keyword: " + keyword)

    keyword = keyword.replace(" ", "%20")
    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + keyword + "&api-key=OQ6qAxiPHDFQFFXB8J9AfZ4mOXwlDEX2"
    jsonurl = urlopen(url)
    fulltext = json.loads(jsonurl.read())

    num_articles = fulltext['response']['meta']['hits'] # Get number of found articles
    if num_articles == 0:
        logging.info("User has supplied keyword with no matching articles")
        return "No articles found."

    articles = fulltext['response']['docs'] # Get the URL's of the articles
    urls = ""

    for article in articles:
        urls += (article['web_url'] + "<br>")

    return urls

def queryPerson(name): # Get a list of articles related to a person's name
    logging.info("User has queried news using a persons name: " + name)

    names = name.split() # Check if valid name
    if len(names) < 2:
        logging.info("User has supplied invalid name for article search")
        return "Error: Invalid Name Given"

    url = "http://api.nytimes.com/svc/semantic/v2/concept/name/nytd_per/" + names[1] + ",%20" + names[0] + ".json?fields=article_list&api-key=OQ6qAxiPHDFQFFXB8J9AfZ4mOXwlDEX2"
    jsonurl = urlopen(url)
    fulltext = json.loads(jsonurl.read())

    num_results = fulltext['num_results'] # Check to see if any articles are found
    if num_results == 0:
        return "No articles found."

    articles = fulltext['results'][0]['article_list']['results'] # Get articles from dictionary
    urls = ""
    
    for article in articles:
        urls += (article['url'] + "<br>")

    return urls

def queryHistorical(keyword, startDate, endDate): # Get a list of articles related to a keyword, during a specific time
    logging.info("User has queried using for historical arcticles")

    keyword = keyword.replace(" ", "%20")
    startDate = startDate.replace("-", "")
    endDate = endDate.replace("-", "")

    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + keyword + "&facet_fields=source&facet=true&begin_date=" + startDate + "&end_date=" + endDate + "&api-key=OQ6qAxiPHDFQFFXB8J9AfZ4mOXwlDEX2"
    jsonurl = urlopen(url)
    fulltext = json.loads(jsonurl.read())

    num_articles = fulltext['response']['meta']['hits'] # Get number of found articles

    if num_articles == 0:
        logging.info("User has supplied keyword with no matching articles")
        return "No articles found."

    articles = fulltext['response']['docs'] # Get the URL's of the articles
    urls = ""

    for article in articles:
        urls += (article['web_url'] + "<br>")

    return urls

