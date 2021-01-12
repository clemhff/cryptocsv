import os

'''from db import query
from queryList import numberRows, selectNLines
from csvUtils import csv_append'''

from loopInsert import loop

csvName = 'dataset.csv'
last = query(numberRows('adausdt'))[0][0] # number of rows in table
increment = 500

#delete csv if csv exist
if os.path.exists(csvName) == True:
    os.remove(csvName)

#Titles csv
Titles=['timestamp', 'open', 'high','low','close','volume','quoteasset','trade','takerbuybase','takerbuyquote']
csv_append(csvName, Titles)

# n lines request and insertion in csv
loop('adausdt', 500 , csvName)
