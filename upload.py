# Secure File Uploader / Ingestor

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is uploading a file. Errors
# can show up when there are network errors, file handling errors, or memory related errors.

# Data

#Functions

def upload(filename): # Upload a PDF file to be converted, or a text file, and saved in the database
    logging.info("User uploaded a file for text translation")

    if filename.endswith(".pdf") or filename.endswith(".txt"):
        return "Upload Successful"
    else:
        return "Invalid Filetype"

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