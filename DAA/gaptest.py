import random
num_list =[4,1,3,5,1,7,2,8,2,0,7,9,1,3,5,2,7,9,4,1,6,3,3,9,6,3,4,8,2,3,1,9,4,4,6,8,4,1,3,8,9,5,5,7,3,9,5,9,8,5,3,2,2,3,7,4,7,0,3,6,3,5,9,9,5,5,5,0,4,6,8,0,4,7,0,3,3,0,9,5,7,9,5,1,6,6,3,8,8,8,9,2,9,1,8,5,4,4,5,0,2,3,9,7,1,2,0,3,6,3] 
 
digits = [0,1,2,3,4,5,6,7,8,9]
 
 
def get_gaps(digit):
    indexes = []
    for ind,num in enumerate(num_list):
        if(num==digit):
            indexes.append(ind)
 
    gaps =[]
 
 
    for pos,ind in enumerate(indexes):
        if (pos+1)!=(len(indexes)):
            gap = (indexes[pos+1]-indexes[pos])-1
            gaps.append(gap)
    return gaps
 
all_gaps=[]
 
for digit in digits:
    for gap in get_gaps(digit):
        all_gaps.append(gap)
 
# print(all_gaps)
 
def gap_length_freq(a,b):
    freq = 0
    for i in range(a,b+1):
        for j in all_gaps:
            if(i==j):
                freq+=1
    return freq
 
max_class = max(all_gaps)
 
while(((max_class+1)%3)!=0):
    max_class+=1
 
def cum_freq(a,b):
    cf = gap_length_freq(a,b)/100
 
    while a!=0:
        a -= 4
        b -= 4
        cf += gap_length_freq(a,b)/100
    return cf
 
def func(b):
    x = b
    return (1 - 0.9 **(x+1))
 
#classes
classes = []
 
 
initial = [0,3]
d_ranks = []
while initial[1] < max_class+4:
    classes.append(initial)
    fx_sub_cf = abs(func(initial[1]) - cum_freq(initial[0],initial[1]))
    d_ranks.append(fx_sub_cf)
    print(initial,gap_length_freq(initial[0],initial[1]),gap_length_freq(initial[0],initial[1])/100,cum_freq(initial[0],initial[1]),func(initial[1]),fx_sub_cf,sep = "\t\t")
    initial[0] += 4
    initial[1] += 4
 
d_calc = max(d_ranks)
d_tab = 1.36/100
 
print(d_calc)
# print(classes)