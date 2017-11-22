import os
from time import sleep
import subprocess
import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


# open a file
# open a file from a website

# open a file from a local directory

# search relevant files with the input file name

# location
os.chdir("/Users/qiyshen")
print(os.getcwd())

# file search
def search_file():
    file_name = ""
    lines = []
    while len(lines) != 1:
        if len(lines) == 0:
            file_name = raw_input("Enter the pdf file to proceed: ")
        else:
            file_name = raw_input("COPY a FULL file PATH from the list of results above to proceed: ")
            # enable user to select options. 
        find_output = subprocess.check_output('find . -iname """*' + file_name + '*""" -print0 | xargs -0 grep -v Caches', shell=True)
        lines = find_output.split('\n')
        word_individual = []
        directory_list = []
        directory_str = ""
        line_1 = ""
        for line in enumerate(lines):
            if "Binary" in line:
                line_1 = line
                return line_1
        for word in line_1.split(" "):
            word_individual.append(word)
        print(word_individual)
        for word in word_individual:
            if word != ("Binary", "file", "matches"):
                directory_list.append(word)
                return directory_list
        directory_str = ' '.join(directory_list)
        find_output = directory_str

        print(find_output)
        # count the number of lines from the output
        
    return file_name 

def read_file():
    print('test')
    local_file_name = file_name
    pdfFileObj = open(local_file_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    pageText = pageObj.extractText()
    print(pageText)


# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = file(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos = set()

#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
#         interpreter.process_page(page)

#     text = retstr.getvalue()

#     fp.close()
#     device.close()
#     retstr.close()
#     return text




# start program

file_name = search_file()

print("Did it work?")
print(file_name)

# print(convert_pdf_to_txt(file_name))
read_file()

    

