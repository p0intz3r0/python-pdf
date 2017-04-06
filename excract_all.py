import pdfquery, csv, os, sys, codecs, unicodecsv, shutil
from cStringIO import StringIO
fct_path = 'C:\Users\FACTURES 2016'
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
res = {'Filename': '', 'TJM': '', 'jours_pr': '', 'collab': '', 'date': '', 'num': '', 'clientid': '', 'sommettc' : ''}
ifile = StringIO()
writer = unicodecsv.writer(ifile, encoding="utf-8")
writer.writerow(list(res.keys()))
for filename in os.listdir(fct_path):
    if filename.endswith(".pdf"):
        filename = fct_path + '/' + filename
        pdf = pdfquery.PDFQuery(filename)
        pdf.load()
        print filename
        label = pdf.pq('LTTextLineHorizontal:contains("Total")')
        res['Filename'] = filename
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        print left_corner
        print bottom_corner
        #print res
       # writer.writerow(res.values())
#with open('C:\Users\p0intz3r0\Desktop\COOPTALIS\FACTURES 2016\extraction_pdf.csv', "wb") as fd:
   # ifile.seek(0)
   # shutil.copyfileobj(ifile, fd)
