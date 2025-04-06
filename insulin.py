# insulin ="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaed" \
# "lqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# print(len(insulin))
# ###lab10
# lsinsulin =insulin[0:24]
# binsulin=insulin[24:54]
# cinsulin=insulin[54:89]
# ainsulin=insulin[89:110]
# print(lsinsulin)
# print(len(lsinsulin))
# print(binsulin)
# print(len(binsulin))
# print(cinsulin)
# print(len(cinsulin))
# print(ainsulin)
# print(len(ainsulin))


# # Calculating the molecular weight of insulin  
# # Creating a list of the amino acid (AA) weights  
# aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
# 'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
# 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
# 'V': 117.15, 'W': 204.23, 'Y': 181.19}

# ##count the value of each amino
# aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaWeights.keys()})
# # Multiply the count by the weights  
# molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in aaWeights.keys()}.values())
# print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
# # print(aaCountInsulin)
# molecularWeightInsulinActual = 5807.63
# print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

# #####use list compriehensen to find cube

# # lst=[6,5,2,8,9,3,2]

# # lst2 = [x**3 for x in lst]
# # print(lst2)

# ##2nd way
# ###print(x**3 for x in [1,2,3,4,5])


# ###use some function
# # list1 =[4,5,2,6,8,3,2]
# #tup=(1,2,3)
# #dictionary={"a":20,"B":30}
# # print(sum(list1))
# #print(sum(tup))
# #print(sum(dictionary.values()))
# # ##wap to find unique character from given two strings
# # str1='ram'
# # str2='hari'

# # str1=str1+str2
# # lst1=[]
# # for i in str1:
# #     if i not in lst1:
# #         lst1.append(i)
# # print(lst1)

# # ##2nd way
# # str="ram"
# # str2="hari"
# # print(set(str+str2))
# # a=[1,2,3,4,5]
# # # print(set(a))


# # Python3.6  
# # Coding: utf-8  
# # Store the human preproinsulin sequence in a variable called preproinsulin:  
# preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# # Store the remaining sequence elements of human insulin in variables:  
# lsInsulin = "malwmrllpllallalwgpdpaaa"  
# bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
# aInsulin = "giveqcctsicslyqlenycn"  
# cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
# insulin = bInsulin + aInsulin


# pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

# seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# pH=0
# while (pH <= 14):
#     netCharge = (
#      +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
#      for x in ['k','h','r']}.values()))
#      -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
#      for x in ['y','c','d','e']}.values())))

#     print('{0:.2f}'.format(netCharge), pH)
#     pH+=1

