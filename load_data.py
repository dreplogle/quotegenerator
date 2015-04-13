# Full path and name to your csv file
csv_filepathname="/Users/dreplogle/Documents/quotes_website/quotes_all.csv"
# Full path to your django project directory
your_djangoproject_home="/Users/dreplogle/Documents/quotes_website"

import sys,os
sys.path.append("quotes_website")
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from quotesearch.models import Quote

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=';', quotechar='"')

for row in dataReader:
    quotelist = Quote()
    quotelist.quote = row[0]
    quotelist.author = row[1]
    quotelist.tag = row[2]
    quotelist.save()
