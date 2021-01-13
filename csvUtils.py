import csv

def csv_append(csvName, list):

    with open('./csv/' + csvName, 'a') as f_object:
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = csv.writer(f_object, delimiter=';')
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(list)
        #Close the file object
        f_object.close()
