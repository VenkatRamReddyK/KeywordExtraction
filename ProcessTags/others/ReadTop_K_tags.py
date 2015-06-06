import csv
# initialized top K tags to a dictionary
def initTagFreqList():
    global topKTagFreqDict;
    global readNoOfTags;
    _tagIndex=0
    # read top readNoOfTags tags    
    with open('../Data/OrderedTagFreqList.csv', 'rb') as f:    
        reader = csv.reader(f)        
        for (_tag,freq) in reader:
            topKTagFreqDict[_tagIndex]=(_tag,freq)        
            if _tagIndex ==readNoOfTags-1:
                break
            _tagIndex=_tagIndex+1  
            
def printTopKFreqWords():         
    global topKTagFreqDict;
    print "- - - - - Tag Frequency Dict - - - - - "        
    for id,tagfreqlist in topKTagFreqDict.items():        
        print id," - >",tagfreqlist

# return top 'index' tag 
def getTag(_index):
    global readNoOfTags;
    if _index<readNoOfTags and _index > 0:
        return topKTagFreqDict[_index-1][0]; 
    else:
        return -1;

def getIndex(_tag):
    for _index,value in topKTagFreqDict.items():
        if value[0]==_tag:
            return _index+1
    return -1; 
        
        
readNoOfTags=42048;#500; 
topKTagFreqDict={}        
initTagFreqList();

printTopKFreqWords();

_index=23;
_tag='ruby';
print "top tag at index: ",_index,"is : ",getTag(_index);        
print "index at tag: ",_tag,"is : ",getIndex(_tag);
