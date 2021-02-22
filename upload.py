# Secure File Uploader / Ingestor

import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
# NOTE: For logs, warnings can show up in instances when a user is inputting a filetype. Errors
#  can show up when there are network errors, file handling errors, or memory related erros. 
# In my test cases I will only be showing informational logs regarding successful use of the module.

# Data

# file -> the file to be converted
status = ""

#Functions

def upload(filename):
    logging.info("User uploaded a file for text translation")

    return "File Upload Successful!"

def checkStatus():
    logging.info("User checked status of file upload")

    return "Failure - File Too Large!"