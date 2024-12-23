import PyPDF2
import sys
import os

dir = input('Enter the path to the directory containing the PDF files: ')
for file in os.listdir(dir):
    if file.endswith('.pdf'):
        PyPDF2.PdfFileMerger().append(file)
    PyPDF2.PdfFileMerger().write(os.path.join(dir,'merged.pdf'))
print('Success!')