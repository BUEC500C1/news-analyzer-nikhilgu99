# Secure File Uploader / Ingestor

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is uploading a file. Errors
# can show up when there are network errors, file handling errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

#Functions

def upload(filename):
    logging.info("User uploaded a file for text translation")

    if filename.endswith(".pdf") or filename.endswith(".txt"):
        return "Upload Successful"
    else:
        return "Invalid Filetype"

def read(filename):
    logging.info("User requested file for retrieval")

    return "Successfully Retrieved"

def update(filename, id, value):
    logging.info("User updated a files information")

    if id == "name":
        return "Successfully Updated"
    else:
        return "Invalid File Attribute"

def delete(filename):
    logging.info("User deleted a file")

    return "Successfully Deleted"