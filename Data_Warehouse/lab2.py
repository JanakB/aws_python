import re
def cidentifier(mystring):
validation ="^([a-zA-Z]|_)+(\d)*$" check = re.search(validation,mystring) keywords
=["auto","double","int","struct","break","else","long","switch","c ase","enum","register","typedef","char","extern","return","union", "continue","for","signed","void","do","if","static","while","defau lt","goto","sizeof","volatile","const","float","short","unsigned"]
if check and mystring not in keywords:
print("Valid C identifier")
else:
print("Invalid C identifier")
def checkmail(email):
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w$' if(re.search(regex,email)):
print("Valid Email")
else:
print("Invalid Email")
def nepalinumber(number):
numregex = '^(98)\d{8}$' if(re.search(numregex,number)):
print("Valid number")
else:
print("Invalid number")
cidentifier(“myvar”) checkmail(“sup@gmail.com”) nepalinumber(“9812345678”)
