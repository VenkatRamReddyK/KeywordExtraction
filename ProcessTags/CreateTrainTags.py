# Reads tags from train.csv and computes creates trainedtags.csv
 
import csv
import nltk
import csv


count=1
with open('../Data/Input/Train.csv', 'rb') as f:    
    reader = csv.reader(f)
    next(reader)
    with open("../Data/Intermediate/trainedtags.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in reader:
            print "Tag Count:",count
            writer.writerow([row[0],row[3]])                            
            count=count+1  