import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist
import re
import string

# read each of the cleaned Question into an instance of TokenList  
class TokenList:        
    def __init__(self):
        self._tokens=[]
        self._id=-1
    def getId(self):
        return self._id    
    def setId(self,id):
        self._id=id    
    def getTokens(self):
        return self._tokens.items()    
    def setTokens(self,tokens):
        self._tokens=tokens
#read each of the tags in the         
class TagFreq:
    def __init__(self,tags,freq):
        self._tags=tags
        self._freq=freq
    def getFreq(self):
        return self._freq    
    def setFreq(self,freq):
        self._freq=freq       
        
    def getTags(self):
        return self._tags    
    def setTags(self,tags):
        self._tags=tags    
        
    def addFreq(self,freq):
        self._freq=self._freq+freq;

def printTags():
    global tagsDict;
    print "- - - - - - -  Tag List - - - - -";
    for key,tags in tagsDict.items():
        print key,tags

def printTokens():    
    print "- - - - - - -  Frequency Distribution List - - - - -";
    for tokens in tokensDict:
        print tokens.getTokens()

# Algorithm to add local tag frequency list to global Type tag frequency list
# {type1 : [(tag1,f1),(tag2,f2),....],type2:[,...] }            
def addToGlobalList(tags,typeFreqDict):
    global typeTagFreqDict;
    for _type,_freq in typeFreqDict.items():

    #  If the type already exists in the global dict
        if typeTagFreqDict.has_key(_type):
            #for each tag in the existing _type
            for i,_tag in enumerate(tags):
                #Searching tag in tag frequency list
#                 if _tag in typeTagFreqDict[_type]:
#                     typeTagFreqDict[_type][_tag]=typeTagFreqDict[_type][_tag]+_freq                
                __tagFreqUpdated=True;
                #  check tag exist or not 
                for i,_tagFreqObj in enumerate(typeTagFreqDict[_type]):                    
                    if _tagFreqObj.getTags()==_tag:# tag found =>Update
#                         print "Type Name"
                        __tagFreqUpdated=False;
                        _tagFreqObj.addFreq(_freq)
                        typeTagFreqDict[_type][i]=_tagFreqObj
                                            
                if __tagFreqUpdated:
                    #Check if the list is empty
                    if i==0:
                        typeTagFreqDict[_type]=[TagFreq(_tag,_freq)]
                    else:
                        typeTagFreqDict[_type].append(TagFreq(_tag,_freq))
        #If the type doesn't exist in the global dict
        else:
#             tagFreqList=[]
#             tagFreq=TagFreq();
            _tagFreqList=[TagFreq(_tag,_freq) for _tag in tags];
            typeTagFreqDict[_type]=_tagFreqList;

def createTypeTagFreqDict():    
    global tokensDict;
    global tagsDict;
    for _index in tokensDict.keys():        
        addToGlobalList((tagsDict[_index]).split(" "), tokensDict[_index])                        
    
# Read from CVS and Creates a Tags List             
def readTagsFromCSV(_filename):
    print "- - - - -  Tag Reading Initiated - - - - -"
    _tagIndex=0
    global tagsDict
    with open('../Data/Intermediate/'+_filename, 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:            
            tagsDict[row[0]]=row[1]
#             print _tokensIndex            
            print _tagIndex
            _tagIndex=_tagIndex+1
    print "- - - - -  Tag Reading Accomplished - - - - -"

def readAndProcessQuestions(_filename):
    print "- - - - - Tokens Reading Initiated - - - - -"
    _tokensIndex=0
    global _qtion
    global tokensDict
    stopset = set(stopwords.words('english'))
    customstopwords=["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"]
    with open('../Data/'+_filename, 'rb') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            _qtion=row[1] # reading question 
            tokens=word_tokenize(_qtion)
            default_filtered_tokens = [w for w in tokens if not w in stopset]                            
            customfiltered_tokens = [w for w in default_filtered_tokens if not w in customstopwords]            
            freqDist=FreqDist(customfiltered_tokens)           
            # add the frequency distribution to TokenList            
            tokensDict[row[0]]=freqDist # title + body
            print _tokensIndex
            _tokensIndex=_tokensIndex+1
            
    print "- - - - - Tokens  Reading Accomplished - - - - -"

# def writeQuestionsToCSV(_filename):
#     with open("../Data/"+_filename, "wb") as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         for _posting in postingsList:                
#             writer.writerow([_posting.getId(),_posting.getQtion()])
#     print "- - - - - - - Write to file accomplished";
    
_qtion=""
tokensDict={}
tagsDict={}
typeTagFreqDict={}
readTagsFromCSV("trainedtags.csv")
printTags()

readAndProcessQuestions("cleanedQuestions.csv")#
 # after cleaning process it further
# printTokens()
createTypeTagFreqDict();
print "- - - - -  Global Type Tag Freq List - - - - -"
for type,tagfreqlist in typeTagFreqDict.items():
    print "type", type
    print "- - - - - Tag Freq: - - -   "
    for tagFreq in tagfreqlist:
        print tagFreq.getTags(),tagFreq.getFreq()
        
        
        