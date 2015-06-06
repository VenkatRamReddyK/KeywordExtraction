import csv
# just change the sample count to create a new sample for train and test qtions and tags 
samplecount=1000
q_read_count_start=0
t_read_count_start=0
# creates training samples of size samplecount 
def createQtions(_filename,startcount):
    count=1
    global samplecount,q_read_count_start; 
    #reading qtions from the main training samples   
    with open('../../src/Data/Intermediate/cleanedtrainquestions.csv', 'rb') as f:    
        reader = csv.reader(f)
                
        with open(_filename, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in reader:
                print count
                if(count==startcount):
                    q_read_count_start=count;
                    print "started reading qtions at:[ ",startcount,"] : from: ",samplecount
                if(count>=startcount):                
                    writer.writerow([row[0],row[1]])                
                if count ==samplecount+startcount-1:
                    break
                count=count+1    

def createTags(_filename,startcount):
    count=1
    global samplecount,t_read_count_start;
    #reading tags from the main train samples  
    with open('../../src/Data/Intermediate/trainedtags.csv', 'rb') as f:    
        reader = csv.reader(f)
        with open(_filename, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for row in reader:    
                print count
                if(count==startcount):
                        t_read_count_start=count;
                        print "started reading tags at:[ ",startcount,"] : from: ",samplecount
                if(count>=startcount):                
                    writer.writerow([row[0],row[1]])                
                if count ==samplecount+startcount-1:
                    break
                count=count+1    
                
# => means train => train samples 
createQtions("../Data/Intermediate/trainqtions.csv",1)
createTags("../Data/Intermediate/traintags.csv",1);

# 0 => means train 1=> test samples
createQtions("../Data/Intermediate/testqtions.csv",samplecount+1)
createTags("../Data/Intermediate/testtags.csv",samplecount+1);

print "Training Samples: "
print "Created tr reading started at: ",q_read_count_start
print "Test Samples: "
print "tags reading started at: ",t_read_count_start