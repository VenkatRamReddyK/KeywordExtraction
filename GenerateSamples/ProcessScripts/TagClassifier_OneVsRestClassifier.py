import csv
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
def readfiles():
    global train_qtions,train_tags,test_qtions;
    #reading training questions
    with open('../Data/Intermediate/trainqtions.csv','rb') as f:
        train_qtion_reader=csv.reader(f)
        for row in train_qtion_reader:
            train_qtions.append(row[1])
    #reading training tags        
    with open('../Data/Intermediate/traintags.csv','rb') as f:
        train_tags_reader=csv.reader(f)
        for row in train_tags_reader:
            train_tags.append(row[1])
    #reading test questions        
    with open('../Data/Intermediate/testqtions.csv','rb') as f:
        test_qtions_reader=csv.reader(f)
        for row in test_qtions_reader:
            test_qtions.append(row[1])
            
    #reading test tags        
    with open('../Data/Intermediate/testtags.csv','rb') as f:
        test_tags_reader=csv.reader(f)
        for row in test_tags_reader:
            test_qtions.append(row[1])        
        

def prediction():
    global train_qtions,train_tags,test_qtions,target_names;

    X_train = np.array(train_qtions)
    y_train =train_tags;   
    X_test = np.array(test_qtions)
    
    classifier = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', LinearSVC())])#LogisticRegression   OneVsRestClassifier()
#      clf = Pipeline([('vect', CountVectorizer(stop_words='english')),('tfidf', TfidfTransformer()), 
#('anova', anova_filter), ('svc', svm.LinearSVC())])           
    
    classifier.fit(X_train, y_train)
    predicted = classifier.predict(X_test)
    for item, labels in zip(X_test, predicted):
        print '%s => %s' % (item, ''.join(x for x in labels)) 

# cross validation
    C_means = list() 
    C_stds = list()                                                                              
        # a pool of C - (Regularization values) are used and the cross-validation test identifies the best C-value that fits for the SVM classifier
    C=(0.025, 0.25, 0.5, 0.6, 0.8, 1.0, 2.0, 3.0, 4.0, 5.0, 10, 100, 1000)   
    for cVal in C:                       
        classifier.set_params(clf__C=cVal)
        # Compute cross-validation score using all CPUs for choosing the best C value
        this_scores = cross_validation.cross_val_score(classifier, X_train, y_train, n_jobs=-1)
        C_means.append(this_scores.mean())
        C_stds.append(this_scores.std())
        
    #Based on the mean-scores find the best C-value
    maxCValue=max(C_means)
    indexCValue=C_means.index(maxCValue)
    finalC = C[indexCValue]
    #set the best C value(Regularization value) to the LinearSVC classifier
    print "\n\n finalC:",finalC    
    classifier.set_params(clf__C=finalC) 



train_qtions=[]
train_tags=[]
test_qtions=[]
test_tags=[]

print " - - - - Reading Files initiated - - - -"
readfiles()
print " - - - - Reading Files accomplished: - - - -"
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
