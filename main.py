import os
from csvUtils import csv_append
from loopInsert import loop

symbol = 'adausdt'
csvName = symbol + '.csv'

#delete csv if csv exist
if os.path.exists(csvName) == True:
    os.remove(csvName)

#Titles csv
Titles=['timestamp', 'open', 'high','low','close','volume','quoteasset','trade','takerbuybase','takerbuyquote']
csv_append(csvName, Titles)

# n lines request and insertion in csv
loop(symbol, 500 , csvName)
