import PyPDF2
import sys



def Merge(pdf_list, name):
    merger = PyPDF2.PdfFileMerger()
    for itm in pdf_list:
        merger.append(itm)
    merger.write(name)
    print("Pdfs merged.")

while True:
    print("Press 0 to exit.")
    pdfs = [itm for itm in input("Enter Path Pdfs:- ").split()]
    if pdfs == ['0']:
        exit()
    name = input("Where do you want to Save merged pdf:- ")
    Merge(pdfs, name)
