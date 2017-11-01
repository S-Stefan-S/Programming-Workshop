import PyPDF2
import sys
import os
from time import sleep
import subprocess


# open a file
# open a file from a website

# open a file from a local directory
file_name = ""
line_count = 0

# search relevant files with the input file name
while line_count != 1:
    if line_count == 0:
        file_name = raw_input("Enter the pdf file to proceed: ")
    else:
        file_name = raw_input("Enter a file from the list of results above to proceed: ")
    os_command_find = subprocess.check_output("find . -name " + file_name + " | xargs grep -v Caches | xargs grep -l '.pdf'")
    print(os_command_find)
    # ount the number of lines from the output
    line_count = (subprocess.check_output("wc -l " + OScommandFind)

# pdfFileObj = open(os_command_find, 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)