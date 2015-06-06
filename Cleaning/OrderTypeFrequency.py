# Reads tags from train.csv and computes tag frequency list and stores it into orderedfreq list 
import csv
import nltk
import csv
from nltk import FreqDist
import re

print "- - - - - Frequency Distribution Initiated - - - - - "
#applying frequency distribution for type     
typeFreqList=FreqDist(typelist);
print "- - - - - Frequency Distribution Accomplished - - - - - "

#printFreqDist()
# sorting Tag frequency list
print "- - - - - Sorting Initiated - - - - - "
sortedTypeFreqList = sorted(typeFreqList.items(), key = lambda x:x[1], reverse = True)
# printSortedFreqDist()
print "- - - - - Sorting Accomplished - - - - - "

    
