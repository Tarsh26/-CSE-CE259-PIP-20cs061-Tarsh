from PyPDF2 import PdfFileReader as pfr
myPdf = pfr("C:/Users/dell/Desktop/Result.pdf")
print(myPdf.getNumPages())
print(myPdf.documentInfo)
for p in myPdf.pages:
    print(p.extractText())
