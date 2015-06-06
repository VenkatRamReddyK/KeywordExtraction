import csv
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
def readfiles():
    global train_qtions,train_tags,test_qtions,input_qtions,input_tags;
    
    #reading input questions
    with open('../../Spimi/Data/Intermediate/chunk_qtions_1.csv','rb') as f:
        input_qtion_reader=csv.reader(f)
        for row in input_qtion_reader:
            input_qtions.append(row[1])
    #reading input tags        
    with open('../../Spimi/Data/Intermediate/chunk_tags_1.csv','rb') as f:
        input_tags_reader=csv.reader(f)
        for row in input_tags_reader:
            input_tags.append(row[1])
            
#reading test questions        
#     with open('../Data/Intermediate/testqtions.csv','rb') as f:
#         test_qtions_reader=csv.reader(f)
#         for row in test_qtions_reader:
#             test_qtions.append(row[1])
#             
#     #reading test tags        
#     with open('../Data/Intermediate/testtags.csv','rb') as f:
#         test_tags_reader=csv.reader(f)
#         for row in test_tags_reader:
#             test_qtions.append(row[1])        
        

def prediction():
    global train_qtions,train_tags,test_qtions,target_names;

    X_train = np.array(train_qtions)
    y_train =train_tags;   
    X_test = np.array(test_qtions)
    
    classifier = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', OneVsRestClassifier(SGDClassifier(loss='huber')))])#LogisticRegression
    print "- - - -  X train lenngth",len(X_train)
    print "- - - -  Y train lenngth",len(y_train)
    print "- - - -  X test lenngth",len(X_test)
    
    classifier.fit(X_train, y_train)
    predicted = classifier.predict(X_test)
    for item, labels in zip(X_test, predicted):
        print '%s => %s' % (item, ''.join(x for x in labels)) 

input_qtions=[]
input_tags=[]

print " - - - - Reading Files initiated - - - -"
readfiles()
print " - - - - Reading Files accomplished: - - - -"


train_count= int(len(input_qtions)*0.7) #1055983;

train_qtions=input_qtions[:train_count] # read 70%  - 1508548 
train_tags=input_tags[:train_count]

test_qtions=input_qtions[train_count+1:]
test_tags=input_tags[train_count+1:] 




# print " - - - - train questions: - - - -"
# for qtion in train_qtions:
#     print qtion;
# print " - - - - train tags: - - - -"
# for tags in train_tags:
#     print tags;
# print ;
# print " - - - - test questions: - - - -"
# for qtion in test_qtions:
#     print qtion;    
# print " - - - - test tags: - - - -"
# for tags in test_tags:
#     print tags;
print " - - - - Prediction Started: - - - -"
prediction()         
