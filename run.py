import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=['GET'])
def home(): # Home page for project 
    return "<h1>News Analyzer Project</h1>"

### FILE UPLOAD API ###

@app.route("/fileupload", methods=['GET'])
def fu_all(): # Home page for File Upload API
    return "<h1>File Uploader API</h1>"

@app.route("/fileupload/upload", methods=['GET'])
def fu_upload(): # Upload file to the database

    if 'filename' in request.args:
        filename = str(request.args['filename'])
        return "Uploaded " + filename
    else:
        return "Error: File Not Found"

@app.route("/fileupload/read", methods=['GET'])
def fu_read(): # Grab file from the database

    if 'filename' in request.args:
        filename = str(request.args['filename'])
        return "Retrieved " + filename
    else:
        return "Error: File Not Found"

@app.route("/fileupload/update", methods=['GET'])
def fu_update(): # Update a files info in the database

    if 'filename' in request.args:
        filename = str(request.args['filename'])
        
        if 'entity' in request.args:
            entity = str(request.args['entity'])
            return "Updated \"" + filename + "\" entity " + entity
        else:
            return "Error: Invalid File Entity Provided"
    else:
        return "Error: File Not Found"

@app.route("/fileupload/delete", methods=['GET'])
def fu_delete(): # Delete a file from the database

    if 'filename' in request.args:
        filename = str(request.args['filename'])
        return "Deleted " + filename
    else:
        return "Error: File Not Found"

### NLP ANALYSIS API ###

@app.route("/nlp", methods=['GET'])
def nlp_all():
    return "<h1>NLP Analysis API</h1>"

@app.route("/nlp/sentiment", methods=['GET'])
def nlp_sentiment():
    if 'text' in request.args:
        return "Score: 0.9 (Positive)"
    else:
        return "Error: No Text Given"

@app.route("/nlp/entity", methods=['GET'])
def nlp_entity():
    if 'text' in request.args:
        return "Found: xyz nouns, xyz names"
    else:
        return "Error: No Text Given"

@app.route("/nlp/entity-sentiment", methods=['GET'])
def nlp_entity_sentiment():
    if 'text' in request.args:
        return "Score: 0.9 (Positive)<br>Found xyz names, xyz nouns."
    else:
        return "Error: No Text Found"

@app.route("/nlp/classify", methods=['GET'])
def nlp_classify():
    if 'text' in request.args:
        return "Topic: Computer Science<br>Confidence: 0.9"
    else:
        return "Error: No Text Found"

### NEWSFEED INGESTOR API ###

@app.route("/newsfeed", methods=['GET'])
def nf_all():
    return "<h1>Newsfeed Ingestor API</h1>"

@app.route("/newsfeed/keywords", methods=['GET'])
def nf_keywords():
    if 'words' in request.args:
        return "Article 1 URL<br>Article 2 URL<br>Article 3 URL"
    else:
        return "Error: No Keywords Supplied"

@app.route("/newsfeed/person", methods=['GET'])
def nf_person():
    if 'name' in request.args:
        return "Article 1 URL<br>Article 2 URL<br>Article 3 URL"
    else:
        return "Error: No Name Given"

@app.route("/newsfeed/historical", methods=['GET'])
def nf_historical():
    if 'year' in request.args and 'month' in request.args and 'words' in request.args:
        return "Article 1 URL<br>Article 2 URL<br>Article 3 URL"
    else:
        return "Error: Missing Information- Year, Month, Keywords"

app.run()