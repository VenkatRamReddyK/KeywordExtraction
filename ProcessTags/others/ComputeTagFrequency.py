# Reads tags from train.csv and computes tag frequency list and stores it into orderedfreq list 
import csv
import nltk
import csv
from nltk import FreqDist

def printFreqDist():
    global tagFreqList;
    print "- - - - -   Freq List Distribution  - - - - "
    for (_tag,_freq) in tagFreqList.items():
        print (_tag,_freq);

def printSortedFreqDist():
    global sortedTagFreqList;
    print "- - - - -   Sorted Tag Freq List Distribution  - - - - "
    for (_tag,_freq) in sortedTagFreqList:
        print (_tag,_freq);

def writeTagstoFile():
    global sortedTagFreqList;
    writeCount=0;    
    print "- - - - - CSV write Initiated - - - - - "
    with open('../Data/OrderedTagFreqList.csv','w') as out:
        csv_out=csv.writer(out)
        for row in sortedTagFreqList:
            csv_out.writerow(row)
            writeCount=writeCount+1
            print "Write Count: ",writeCount
    print "- - - - CSV write Accomplished - - - -  -";

taglist=[]
_qtionCount=0
with open('../Train/Train.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader)
    
    for row in reader: # reading every posting        
        _tags=(row[3]).split(" ");
        taglist.extend(_tags) # splits tags in every postings and appends to taglist        
        print "Reading Count: ",_qtionCount
        _qtionCount=_qtionCount+1
        
        
print "- - - - - Frequency Distribution Initiated - - - - - "
#applying frequency distribution for tags     
tagFreqList=FreqDist(taglist);
print "- - - - - Frequency Distribution Accomplished - - - - - "

# printFreqDist()
# sorting Tag frequency list
print "- - - - - Sorting Initiated - - - - - "
sortedTagFreqList = sorted(tagFreqList.items(), key = lambda x:x[1], reverse = True)
# printSortedFreqDist()
print "- - - - - Sorting Accomplished - - - - - "
writeTagstoFile()
    
