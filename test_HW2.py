import upload as fu # fu = file upload
import NLP as nlp   # nlp = NLP
import news as nf   # nf = news feed 

def testModules(): 
    
    # Secure File Uploader Tests

    assert fu.upload("test.pdf") == "Upload Successful"
    assert fu.upload("file.png") == "Error: Invalid filetype uploaded!"
    assert fu.read("file.txt") == "Successfully Retrieved"
    assert fu.update("file.txt", "name", "new.txt") == "Successfully Updated"
    assert fu.update("file.txt", "size", "2mb") == "Invalid File Attribute"
    assert fu.delete("new.txt") == "Successfully Deleted"

    # NLP Tests

    assert nlp.getSentiment("sentence") == "Score: 0.9 (Positive)"
    assert nlp.getEntities("sentence") == "Found xyz names, xyz nouns, xyz place."
    assert nlp.getEntitySentiment("sentence") == "Score: 0.9 (Positive)- Found xyz names, xyz nouns."
    assert nlp.getClassification("sentence") == "Topic: Computer Science - Confidence: 0.9"

    # Newsfeed Ingestor Tests

    assert nf.queryKeywords(["word1", "word2"]) == "Article 1 URL | Article 2 URL | Article 3 URL"
    assert nf.queryPerson("Nikhil Gupta") == "Article 1 URL | Article 2 URL | Article 3 URL"
    assert nf.queryHistorical(2019,11,["word1", "word2"]) == "Article 1 URL | Article 2 URL | Article 3 URL"