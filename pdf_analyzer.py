import os
from time import sleep
import subprocess
import PyPDF2


# open a file
# open a file from a website

# open a file from a local directory
file_name = ""
lines = []

# search relevant files with the input file name
os.chdir("/Users/qiyshen")
print(os.getcwd())

while len(lines) != 2:
    if len(lines) == 0:
        file_name = raw_input("Enter the pdf file to proceed: ")
    else:
        file_name = raw_input("COPY a FULL file name from the list of results above to proceed: ")
        #enable user to select options. 
    find_output = subprocess.check_output("find . -name *" + file_name + "* | xargs grep -v Caches | awk '{print $3}'", shell=True)
    print(find_output)
    # count the number of lines from the output
    lines = find_output.split('\n')
    
        
pdfFileObj = open(file_name, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
