#Have to Specify what library the function is imported from.
from pypdf import PdfReader
Reader= PdfReader('Practice pdf/processes-09-00858-review paper.pdf')
#Length (len); .pages refers to the number of pages of the pdf file
print(len(Reader.pages))
#Defining specific pages as a variable set
page_1=Reader.pages[0]
#text extraction from pdf
#print(page_1.extract_text())
for i in range(len(Reader.pages)):
    pages=Reader.pages[i]
    #print(pages.extract_text())
#images
for i in pages.images:
    with open(i.name,'wb') as f:
        f.write(i.data)