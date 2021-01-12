from db import query
from queryList import numberRows, selectNLines
from csvUtils import csv_append

def loop(symbol, increment, csvName):

    last = query(numberRows('adausdt'))[0][0] # number of rows in table
    #batch to make small request to the database
    for i in range(0, last, increment):

        part = query(selectNLines('adausdt',i,i+increment))

        for j in range(0,len(part)):

            list=[part[j][1], part[j][2] , part[j][3], part[j][4], part[j][5], part[j][6], part[j][7], part[j][8], part[j][9], part[j][10], ]
            csv_append('./' + csvName, list)

        print(i+increment)

    #print(part[0])
