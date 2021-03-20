import camelot


# pdf file path
file = "file.pdf"    

# reading pdf file
tables = camelot.read_pdf(file, pages='all', line_scale=18, line_tol=3)
# while we convert file from pdf to json is important to know if you need line scale or not

# Loop through all the tables and copy them to a json file

for i in range(len(tables)):
    tables[i].to_json(f'file{i}.json', indent=4)


# This is the messy way of creating new files
#tables.export('filesss.json', f='json', compress=False)    # works for csv, tsv, xsml










