# Reads tags from train.csv and computes tag frequency list and stores it into orderedfreq list 
import csv
import nltk
import csv
from nltk import FreqDist

def printFreqDist():
    global typeFreqList;
    print "- - - - -   Freq List Distribution  - - - - "
    for (_type,_freq) in typeFreqList.items():
        print (_type,_freq);

def printSortedFreqDist():
    global sortedTypeFreqList;
    print "- - - - -   Sorted Type Freq List Distribution  - - - - "
    for (_type,_freq) in sortedTypeFreqList:
        print (_type,_freq);

def writeTypestoFile():
    global typeFreqList;
    writeCount=0;    
    print "- - - - - CSV write Initiated - - - - - "
    with open('../Data/Intermediate/TypeFreqList.csv','w') as out:
        csv_out=csv.writer(out)
        for row in typeFreqList:
            csv_out.writerow(row)
            writeCount=writeCount+1
            print "Write Count: ",writeCount
    print "- - - - CSV write Accomplished - - - -  -";
    
def writeOrderedTypestoFile():
    global sortedTypeFreqList;
    writeCount=0;    
    print "- - - - - CSV write Initiated - - - - - "
    with open('../Data/Intermediate/OrderedTypeFreqList.csv','w') as out:
        csv_out=csv.writer(out)
        for row in sortedTypeFreqList:
            csv_out.writerow(row)
            writeCount=writeCount+1
            print "Write Count: ",writeCount
    print "- - - - CSV write Accomplished - - - -  -";    

typelist=[]
_qtionCount=0
with open('../Data/Intermediate/cleanedtrainquestions.csv', 'rb') as f:
    reader = csv.reader(f)    
    for row in reader: # reading every posting        
        _types=(row[1]).split(" ");# Question
        typelist.extend(_types) # splits type in every postings and appends to typelist        
        print "Reading Count: ",_qtionCount
        _qtionCount=_qtionCount+1
        
        
print "- - - - - Frequency Distribution Initiated - - - - - "
#applying frequency distribution for type     
typeFreqList=FreqDist(typelist);
print "- - - - - Frequency Distribution Accomplished - - - - - "

# printFreqDist()
# sorting Tag frequency list
# print "- - - - - Sorting Initiated - - - - - "
# sortedTypeFreqList = sorted(typeFreqList.items(), key = lambda x:x[1], reverse = True)
# printSortedFreqDist()
# print "- - - - - Sorting Accomplished - - - - - "
writeTypestoFile()
    
