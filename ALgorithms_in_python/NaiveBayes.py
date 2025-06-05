from math import sqrt,exp,pi


# dataset format {outlook,temp,humidity,windy,playGolf}

# Outlook: 0 = Rain, 1 = Overcast, 2 =Sunny
# temp: 0 = Cold, 1=Mild, 2=Hot
# Humidity: 0 = Normal, 1 = High
# Windy: 0 = False, 1 = True
#Golf: 0 = No, 1 = Yes

dataset = [
    [0,2,1,0,0],#0
    [0,2,1,1,0],#1
    [1,2,1,0,1],#2
    [2,0,1,0,1],#3
    [2,0,0,0,1],#4
    [2,0,0,1,0],#5
    [1,0,0,1,1],#6
    [0,1,1,0,0],#7
    [0,0,0,0,1],#8
    [1,1,0,0,1],#9
    [0,1,0,1,1],#10
    [1,1,1,1,1],#11
    [1,2,1,0,1],#12
    [2,1,1,1,0]#13
]

def seperate_by_class(dataset):
    seperated = dict()
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        if class_value not in seperated:
            seperated[class_value] = list()
        seperated[class_value].append(vector)
    return seperated

#seperated = seperate_by_class(dataset)
#for label in seperated:
#    print(label)
#    for row in seperated[label]:
#        print(row)

def mean(numbers):
    return sum(numbers)/float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    variance = sum([(x-avg)**2 for x in numbers])/float(len(numbers)-1)
    return sqrt(variance)

def summarize_dataset(dataset):
    summaries = [(mean(column),stdev(column),len(column)) for column in zip(*dataset)]
    del(summaries[-1])
    return summaries

#summary = summarize_dataset(dataset)
#print(summary)

def summarize_by_class(dataset):
    seperated = seperate_by_class(dataset)
    summaries  = dict()
    for class_value,rows in seperated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries

def gaussian_probability(x,mean,stdev):
    exponent = exp(-((x-mean)**2 / (2 * stdev**2 ))) 
    return (1/(sqrt(2*pi)*stdev)) * exponent

def calculate_class_probabilities(summaries,row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value,class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean,stdev,count =class_summaries[i]
            probabilities[class_value]*=gaussian_probability(row[i],mean,stdev)
        return probabilities

summaries = summarize_by_class(dataset)
probabilities = calculate_class_probabilities(summaries,dataset[0])
print(probabilities)