import PyPDF2, csv, os
fct_path = r'C:\Users\p0intz3r0\Desktop\FACTLOG'
res = []
for filename in os.listdir(fct_path):
    if filename.endswith(".pdf"):
        filename = fct_path + '/' + filename
        print(filename)
        pdfFileObj = open(filename, 'rb')
        print(filename)
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        res.append(pageObj.extractText())
print(res)
