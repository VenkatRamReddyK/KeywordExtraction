from ReadTop_K_tags import *
taglist=[]
_qtionCount=0

with open('../Train/Train.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader)    
    for row in reader: # reading every posting
        with open('../Data/OrderedTagFreqList.csv','w') as out:                
            _tags=(row[3]).split(" ");                
            print "Reading Count: ",_qtionCount
            _qtionCount=_qtionCount+1                        
            hashCodeForTags=[getIndex(_tag) for _tag in _tags]                    
            print hashCodeForTags
            csv_out=csv.writer(out)            
            csv_out.writerow(hashCodeForTags)
