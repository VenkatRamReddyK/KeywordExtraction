import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import re
import string

class Posting:        
    def __init__(self):
        self._qtion=""
        self._id=-1
    def getId(self):
        return self._id    
    def setId(self,id):
        self._id=id    
    def getQtion(self):
        return self._qtion    
    def setQtion(self,qtion):
        self._qtion=qtion

# Read from CVS and Creates a postingsList             
def readQuestionsFromCSV(_filename):
    print "- - - - -  Reading Initiated - - - - -"
    qtionsCount=0
    global postingsList
    with open('../Data/'+_filename, 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            posting=Posting();
            posting.setQtion(row[1]+ " "+row[2]) # title + body
            posting.setId(row[0]) # setting the id of posting            
            postingsList.append(posting)
            print qtionsCount
            qtionsCount=qtionsCount+1
    print "- - - - -  Reading Accomplished - - - - -"

def writeQuestionsToCSV(_filename):
    with open("../Data/"+_filename, "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for _posting in postingsList:                
            writer.writerow([_posting.getId(),_posting.getQtion()])
    print "- - - - - - - Write to file accomplished";
    
#Method for striping out html tags from the questions            

def striphtml():
    global _qtion;
    pattern = re.compile('<.*?>|\\n|\\r|\?|[=\'\"\|:;\$\%\^\`\~\&,\.\\\\()/\[\]\!0-9{}\>\<]')
    _qtion = re.sub(pattern,' ', _qtion)

def stripURLs():
    global _qtion;    
    _qtion=re.sub(r'(https?://\S+)',' ', _qtion);
    
#Method for removing the source code <code> ...</code> from the question     

def removeCodeSection():
    global _qtion;            
    start_seperator='<code>'
    end_seperator='</code>'
    result=[]
    tokenList=_qtion.split(start_seperator)
    for token in tokenList:
        if end_seperator in token:
            result.append(token.split(end_seperator)[1])
        else:
            result.append(token)
    #Append the lines with space in between     
    _qtion=" ".join(result)        
            
# Algorithm to add local tag frequency list to global Type tag frequency list
# {type1 : [(tag1,f1),(tag2,f2),....],type2:[,...] }            
                
def cleanQtions():
    print "- - - - -  Cleaned Initiated - - - - -" 
    _cleaningCount=0
    global _qtion;
    print "Len of postings list: ",len(postingsList)
    for _posting in postingsList:
        _cleaningCount=_cleaningCount+1
        print _cleaningCount        
        _qtion=_posting.getQtion().lower()        
        removeCodeSection();        
        striphtml();                
        stripURLs();
#         print _qtion
        _posting.setQtion(_qtion);
        
    print "- - - - -  Cleaned Accomplished - - - - -"
    
_qtion=""
postingsList=[] # qtionsList
readQuestionsFromCSV("Input/Train.csv")

cleanQtions()
# 
# print "- - - - - - - Cleaned Questions - - - - - - - - " 
# for _posting in postingsList: 
#     print "\n"+_posting.getQtion()

writeQuestionsToCSV("Intermediate/cleanedtrainquestions.csv") # cleaning on total data set

# update readQuestions for reading 


