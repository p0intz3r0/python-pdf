import pdfquery, csv, os, sys, codecs, unicodecsv, shutil
from cStringIO import StringIO
fct_path = 'C:\Users\'
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
        label = pdf.pq('LTTextLineHorizontal:contains("TJM")')
        res['Filename'] = filename
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        TJM = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner-10, bottom_corner-40, left_corner+30, bottom_corner+50)).text()
        res['TJM'] = TJM
        label = pdf.pq('LTTextLineHorizontal:contains("Jours prest")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        jp = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner-10, bottom_corner-40, left_corner+60, bottom_corner+50)).text()
        res['jours_rp'] = jp
        label = pdf.pq('LTTextLineHorizontal:contains("Collabor")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        collab = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (left_corner-10, bottom_corner-40, left_corner+70, bottom_corner+100)).text()
        res['collab'] = collab
        label = pdf.pq('LTTextLineHorizontal:contains("Le")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        date_invoice = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (left_corner+30, bottom_corner, left_corner+110, bottom_corner+110)).text()
        res['date'] = date_invoice
        label = pdf.pq('LTTextLineHorizontal:contains("Facture n")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        num = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (left_corner+30, bottom_corner, left_corner+110, bottom_corner)).text()
        res['num'] = num
        label = pdf.pq('LTTextLineHorizontal:contains("Client n")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        client_id = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (left_corner+30, bottom_corner, left_corner+110, bottom_corner)).text()
        res['clientid'] = client_id
        label = pdf.pq('LTTextLineHorizontal:contains("TOTAL (incl. TVA)")')
        left_corner = float(label.attr('x0'))
        bottom_corner = float(label.attr('y0'))
        montantTTC = pdf.pq('LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (left_corner+90, bottom_corner, left_corner+500, bottom_corner+12)).text()
        res['sommettc'] = montantTTC
        print res
        writer.writerow(res.values())
with open('C:\Users\extraction_pdf.csv', "wb") as fd:
    ifile.seek(0)
    shutil.copyfileobj(ifile, fd)
