from upload import upload, checkStatus
from NLP import uploadNLP, getFullAnalysis, getTranslation, getRelevantLinks, getSentiment
from news import addURL, findKeywords, findNews, findSentiment

# I will do both individual tests and a simulation of 3 modules working together where applicable

def testModules(): 
    # Upload individual tests

    assert checkStatus() == "Failure - File Too Large!"

    # NLP individual tests

    data = getFullAnalysis()

    assert data.sentiment == "call sentiment function here"
    assert data.relevantLinks == ["call link", "function here"]

    # News individual tests - None

    # Combination tests

    assert upload("test.docx") == "File Upload Successful!" # Upload a file to be translated to a txt file

    assert uploadNLP("test.txt") == "File successfully uploaded for NLP analysis." # Upload a txt for NLP
    assert getTranslation("Spanish") == "Translation successful" # Translate the file
    assert getSentiment() == "Positive" # Get the sentiment of the text file
    assert getRelevantLinks(2) == "Successfully found and saved links" # Get some related documents

    assert addURL("url", "links.txt") == "Successfully added URL" # Add URL to text file, could use this in for loop with previous function
    assert findKeywords(5) == ["word1", "word2"] # Find keywords amongst the URL's articles from previous function
    assert findNews(5, ["word1", "word2"], "news.txt") == "Successfully found and added news" # Find related news articles using the keywords from the previous function
    assert findSentiment("news.txt") == "Determined Sentiment: Positive" # Gather an overall sentiment from the found news articles of the previous function