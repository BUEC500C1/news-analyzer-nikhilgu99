import upload as fu # fu = file upload
import NLP as nlp   # nlp = NLP
import news as nf   # nf = news feed 

def testModules(): 
    
    # Secure File Uploader Tests

    assert fu.upload("test.pdf") == "Upload Successful" # Created with file_id = 2
    assert fu.upload("file.png") == "Error: Invalid filetype uploaded!"
    assert fu.read(2) == "Successfully Retrieved"
    assert fu.read(1000) == "Error: No file found under the given file ID!"
    assert fu.update(1, "filename", "newname") == "Successfully Updated"
    assert fu.update(1, "size", "2mb") == "Error: Invalid File Attribute"
    assert fu.delete(2) == "Successfully Deleted" # Delete the entry created above

    # NLP Tests

    assert nlp.getSentiment("sentence") == "Score: 0.9 (Positive)"
    assert nlp.getEntities("sentence") == "Found xyz names, xyz nouns, xyz place."
    assert nlp.getEntitySentiment("sentence") == "Score: 0.9 (Positive)- Found xyz names, xyz nouns."
    assert nlp.getClassification("sentence") == "Topic: Computer Science - Confidence: 0.9"

    # Newsfeed Ingestor Tests

    assert nf.queryKeywords(["word1", "word2"]) == "Article 1 URL | Article 2 URL | Article 3 URL"
    assert nf.queryPerson("Nikhil Gupta") == "Article 1 URL | Article 2 URL | Article 3 URL"
    assert nf.queryHistorical(2019,11,["word1", "word2"]) == "Article 1 URL | Article 2 URL | Article 3 URL"