#Replaces newline with , and populates type count 
import csv
def createStopWords():
    count=1
    global samplecount;
    outputString="" # comma seperated 
    with open('../Data/Intermediate/OrderedTypeFreqList.csv', 'rb') as f:    
        reader = csv.reader(f)
        for row in reader:
            outputString=outputString+row[0]+","
            print count
#             print outputString+"\n"            
            count=count+1
            
    with open("../Data/Intermediate/Nstopwords.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')            
        writer.writerow([outputString])                        

samplecount=-1;
createStopWords();