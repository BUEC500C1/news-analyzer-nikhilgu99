# Secure File Uploader / Ingestor

import datetime
import logging
import PyPDF2
import sqlite3

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is uploading a file. Errors
# can show up when there are network errors, file handling errors, or memory related errors.

#Functions

def upload(filename): # Upload a PDF file to be converted, or a text file, and saved in the database
    logging.info("User uploaded a file for PDF to text conversion")

    date = datetime.datetime.now()
    con = None
    pdfObj = None

    try:
        con = sqlite3.connect('app.db') # Connect to the database
    except:
        logging.error("ERROR: Failed to connect to database")
        return "Error: Failed to connect to database!"

    cursor = con.cursor()
    cursor.execute('SELECT * FROM files') # To get the number of rows for the file_id

    try:
        pdfObj = open('uploads/' + filename, 'rb') # Open the file in binary mode
    except:
        logging.error("ERROR: Invalid filetype uploaded")
        return "Error: Invalid filetype uploaded!"

    input = PyPDF2.PdfFileReader(pdfObj) # Create the PyPDF2 compatible object
    data = ""
    for x in range(input.numPages): # Get text from all the PDF pages
        data += input.getPage(x).extractText()

    #print("file_id: " + str(len(cursor.fetchall()) + 1))
    #print("filename: " + filename)
    #print("upload_date: " + date.strftime('%x'))
    #print("data: " + data)
    entry = (len(cursor.fetchall()), filename, date.strftime('%x'), data) # Secure way of inserting
    cursor.execute('INSERT INTO files VALUES (?,?,?,?)', entry)
    con.commit()
    con.close()
    pdfObj.close()

    logging.info("Successfully uploaded a file to the database")

    return "Upload Successful"

def read(file_id): # Read a text file from the database
    logging.info("User requested file for retrieval")

    con = None

    try:
        con = sqlite3.connect('app.db') # Connect to the database
    except:
        logging.error("ERROR: Failed to connect to database")
        return "Error: Failed to connect to database!"

    fileSecure = (file_id,) # Secure way of doing SQL query
    cursor = con.cursor()
    cursor.execute('SELECT data FROM files WHERE file_id=?', fileSecure)
    data = cursor.fetchone()

    if(data is None):
        con.close()
        logging.error("ERROR: No file found under the given file ID")
        return "Error: No file found under the given file ID!"
    else:
        con.close()
        logging.info("File successfully retrieved from the database")
        return data[0] # data is a tuple, get the text from it

def update(file_id, id, value): # Update the attributes / metadata of a text file

    if (id == "filename") or (id == "upload_date") or (id == "data"):

        con = None

        try:
            con = sqlite3.connect('app.db') # Connect to the database
        except:
            logging.error("ERROR: Failed to connect to database")
            return "Error: Failed to connect to database!"

        fileSecure = (value,file_id) # Secure way of doing SQL query
        cursor = con.cursor()
        query = 'UPDATE files SET ' + id + ' = ? WHERE file_id = ?'
        cursor.execute(query, fileSecure)
        con.commit()
        con.close()
        logging.info("User updated a files attribute")
        return "Successfully Updated"
        
    else:
        logging.error("ERROR: Invalid file attribute given for update parameter")
        return "Error: Invalid File Attribute"

def delete(file_id): # Delete a file from the database

    con = None

    try:
        con = sqlite3.connect('app.db') # Connect to the database
    except:
        logging.error("ERROR: Failed to connect to database")
        return "Error: Failed to connect to database!"

    fileSecure = (file_id,) # Secure way of doing SQL query
    cursor = con.cursor()
    cursor.execute('DELETE FROM files WHERE file_id=?', fileSecure)
    con.commit()
    con.close()
    logging.info("User deleted a file record")

    return "Successfully Deleted"