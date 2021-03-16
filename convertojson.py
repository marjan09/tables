import camelot


# pdf file path
file = "file.pdf"    


# reading pdf file and specific pages
tables = camelot.read_pdf(file, pages='2-end', line_scale=40)
# while we convert file from pdf to json is important to know if you need line scale or not


# exprting pdf file and compressing
tables.export('files.json', f='json', compress=False) # works for csv, tsv, xsml







