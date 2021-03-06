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
        pdfObj = open(filename, 'rb')
    except:
        logging.error("ERROR: Invalid filetype uploaded")
        return "Error: Invalid filetype uploaded!"

    input = PyPDF2.PdfFileReader(pdfObj)
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

    logging.info("Successfully uploaded a file to the database")

    return "Upload Successful"

def read(filename): # Read a text file from the database
    logging.info("User requested file for retrieval")

    return "Successfully Retrieved"

def update(filename, id, value): # Update the attributes / metadata of a text file
    logging.info("User updated a files information")

    if id == "name":
        return "Successfully Updated"
    else:
        return "Invalid File Attribute"

def delete(filename): # Delete a file from the database
    logging.info("User deleted a file")

    return "Successfully Deleted"