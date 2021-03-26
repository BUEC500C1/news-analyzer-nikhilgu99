import flask
import os
import sqlite3
import upload as fu # file upload
import news as nf # newsfeed
import NLP as nlp # nlp analysis

from flask import render_template, request
from werkzeug.utils import secure_filename

app = flask.Flask(__name__, template_folder="html")
app.config["DEBUG"] = True
app.config["UPLOAD_FOLDER"] = "/Users/Nikhil/git/news-analyzer-nikhilgu99/uploads"

@app.route("/", methods=['GET'])
def home(): # Home page for project 
    return render_template('main.html')

### FILE UPLOAD API ###

@app.route("/fileupload", methods=['GET'])
def fu_all(): # Home page for File Upload API
    return render_template('fileupload.html')

@app.route("/fileupload/upload", methods=['GET', 'POST'])
def fu_upload(): # Upload file to the database

    if request.method == 'POST':
        f = request.files['file']

        if f.filename.endswith(".pdf"): # Error checking the filetype 
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return fu.upload(f.filename) # Call the API and upload the file
        else:
            return "Invalid file uploaded, PDF files only"
    else: # GET request, do nothing here
        return "Go back to the home page to upload a file!"

@app.route("/fileupload/read", methods=['GET', 'POST'])
def fu_read(): # Grab file from the database

    if request.method == 'POST':
        fileid = request.form['fileid']
        return fu.read(fileid) # Call the API and read the file
    else: # GET request, do nothing here
        return "Go back to the home page to retrieve a file!"

@app.route("/fileupload/update", methods=['GET', 'POST'])
def fu_update(): # Update a files info in the database

    if request.method == 'POST':
        file_id = request.form['fileid']
        id = request.form['attributes']
        value = request.form['value']
        return fu.update(file_id,id,value) # Call the API and update the file
    else: # GET request, do nothing here
        return "Go back to the home page to update a file!"

@app.route("/fileupload/delete", methods=['GET','POST'])
def fu_delete(): # Delete a file from the database

    if request.method == 'POST':
        file_id = request.form['fileid']
        return fu.delete(file_id) # Call the API and delete the file
    else: # GET request, do nothing here
        return "Go back to the home page to update a file!"

### NLP ANALYSIS API ###

@app.route("/nlp", methods=['GET'])
def nlp_all():
    return render_template('nlp.html')

@app.route("/nlp/sentiment", methods=['GET','POST'])
def nlp_sentiment():
    if request.method == 'POST':
        inp = request.form['input']
        return nlp.getSentiment(inp) # Call the API and run NLP entity analysis
    else: # GET request, do nothing here
        return "Go back to the home page to do sentiment analysis!"

@app.route("/nlp/entity", methods=['GET','POST'])
def nlp_entity():
    if request.method == 'POST':
        inp = request.form['input']
        return nlp.getEntities(inp) # Call the API and run NLP entity analysis
    else: # GET request, do nothing here
        return "Go back to the home page to do entity analysis!"

@app.route("/nlp/entity-sentiment", methods=['GET','POST'])
def nlp_entity_sentiment():
    if request.method == 'POST':
        inp = request.form['input']
        return nlp.getEntitySentiment(inp) # Call the API and run NLP entity-sentiment analysis
    else: # GET request, do nothing here
        return "Go back to the home page to do entity-sentiment analysis!"

@app.route("/nlp/classify", methods=['GET','POST'])
def nlp_classify():
    if request.method == 'POST':
        inp = request.form['input']
        return nlp.getClassification(inp) # Call the API and run NLP classifcation analysis
    else: # GET request, do nothing here
        return "Go back to the home page to do classification analysis!"

### NEWSFEED INGESTOR API ###

@app.route("/newsfeed", methods=['GET'])
def nf_all():
    return render_template('newsfeed.html')

@app.route("/newsfeed/keyword", methods=['GET','POST'])
def nf_keyword():
    if request.method == 'POST':
        keyword = request.form['keyword']
        return nf.queryKeyword(keyword) # Call the API and get articles
    else: # GET request, do nothing here
        return "Go back to the home page to search for articles!"

@app.route("/newsfeed/person", methods=['GET','POST'])
def nf_person(): # Search for related articles to a person
    if request.method == 'POST':
        personName = request.form['personName']
        return nf.queryPerson(personName) # Call the API and get articles
    else: # GET request, do nothing here
        return "Go back to the home page to search for a person!"

@app.route("/newsfeed/historical", methods=['GET','POST'])
def nf_historical():
    if request.method == 'POST':
        keyword = request.form['keyword']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        return nf.queryHistorical(keyword, startDate, endDate) # Call the API and get articles
    else: # GET request, do nothing here
        return "Go back to the home page to update a file!"

app.run()