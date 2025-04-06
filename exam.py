# Given a list [1,2,3,4,5,6,7] randomly choose element from this list and create a new list of length
# # 7. There shouldn’t be any repetitive element.(Don’t use random.shuffle())
# import random
# list = [1,2,3,4,5,6,7]

# random_list = []
# while len(random_list)<7:
# 	var=random.choice(list)
# 	if var in random_list:
# 		continue
# 	else:
# 		random_list.append(var)
# 	print(random_list)


# # 2. Can there be two keys with same name. Justify with program.
# key ={
#     'name':'ram',
#     'age': 25
# }
# print(key)

# key ={
#     'address':'kathmandu',
#     'phone_no': 9867353231
# }
# print(key)

# 3. Given a tuple (44,4,5,6,7) manipulate this tuple to find square of every element and replace the
# # # tuple with squared value.
# tuple1 = (44,4,5,6,7)
# tlist =list(tuple1)
# print(tlist)
# for i in range(len(tlist)):
#     tlist[i]= int(tlist[i]*tlist[i])
    
# print(type(tlist))
# tuple2=tuple(tlist)

# print(type(tuple2))

# # 4. Check whether a given number is perfect cube or not.
# num = int(input("enter any number:"))
# temp = num**(1/3)
# if(int(temp)**3)== num:
#     print("number is perfect cube.")
# else:
#     print("number is not perfect cube.")

# # 5. From two list find the minimum and maximum value.
# list1 = [7,4,2,8,9,12,5]
# list2 = [8,2,6,7,4,8,9,2]
# list3= list1+list2
# print(min(list3))
# print(max(list3))


# 6. Take input from user in the form of string both in upper and lowercase. Now separate upper and
# # lowercase characters.
# user_int = input("enter any strings:")
# upper=[]
# lower=[]
# for char in user_int:
#     if char ==" ":
#         continue
#     if char .isupper()==True:
#         upper.append(char)
#     else:
#         lower.append(char)
# print(upper)
# print(lower)
    

# 7. For a list [3,4,5,6,7] create nested list to show multiplication table of every element up-to 10.
# # output format- [[3,6,9,…..30],………..]
# list = [3,4,5,6,7]
# table=[]
# for i in list:
#     list1=[]
#     for j in range(1,11):
#         list1.append(i*j)
#     print(list1)
#     table.append(list1)
# print(table)
# # 8. Convert 122430120 minutes into years months days hours and minutes.
# mins = 122430120
# hrs = int(mins/60)
# day = int(hrs/24)
# mon = int(day/30)
# yrs = int(mon/12)
# print(f"122430120 mins = {yrs} years {mon} month {day} days {hrs} hour.")


# y=0
# m=0
# d=0
# h=0
# mn=122430120

# def min2hr(min):
# 	h=int(min/60)
# 	min=min%60
# 	# print(h)
# 	print(min)
	
# 	d=int(h/24)
# 	hr=h%24
# 	# print(d)
# 	print(hr)

# 	m=int(d/30)
# 	day=m%30
# 	# print(m)
# 	print(day)

# 	y=int(m/12)
# 	mth=m%12
# 	print(y)
# 	print(mth)
# 	print(y,mth, day,hr,min)
# min2hr(mn)


# # 9. Given a=20A, A=20b, b=16C, C=29d, d=33. For “aabACdCA” find the numerical value.
# d=33
# C=29*d
# b=16*C
# A=20*b
# a=20*A
# print(a*a*b*A*C*d*C*A)

# # var = input("enter characters:")
# # print((var.count("a")*20)+(var.count("A")*20)+(var.count("C")*29)+(var.count("d")*33))


# 10.You are tasked with writing a Python program to calculate the area of different geometric shapes:
# rectangles, circles, and triangles. Each shape has a different formula for calculating its area.
# l= int(input("enter length:"))
# b = int(input("enter breadth:"))
# h= int(input("enter height:"))
# rec_area= print(l*b*h)

# bre = int(input("enter breadth:"))
# he= int(input("enter height:"))
# tri_area=print(1/2*bre*he)

# r = int (input("enter the radius:"))
# pi = 3.14
# cir_area = print("pi*r*r")


# Write a Python program that does the following:
# Defines three functions: calculate_rectangle_area(), calculate_circle_area(), and
# calculate_triangle_area(), each of which takes the necessary parameters and returns the area of the
# respective shape.
# Prompt the user to choose a shape (rectangle, circle, or triangle).
# Depending on the user's choice, take the required input (e.g., length and width for a rectangle,
# radius for a circle, or base and height for a triangle) and call the corresponding function to calculate
# the area.
# Display the calculated area to the user.
# Here are the formulas for each shape:
# Rectangle Area: length x width
# # Circle Area: π x radius^2 (you can use math.pi for π)
# # Triangle Area: 0.5 x base x height
# def calculate_rectangle_area(l,b):
# 		return (l*b)
	
# def calculate_circle_are(r):
# 		return 3.14*r
	
# def calculate_triangle_area(b,h):
# 		return 0.5*b*h
	


# shape=int(input("Enter 1 for rectangle, 2 for circle, 3 for triangle:"))
# if shape==1:
# 	l=int(input("Enter length:"))
# 	b=int(input("Enter breadth"))
# 	print(f"Area of rectangle is:{calculate_rectangle_area(l,b)}")
# elif shape==2:
# 	r=float(input("Enter radius:"))
# 	print(f"Area of circleis: {calculate_circle_are(r)}")
# elif shape==3:
# 	b=float(input("Enter base:"))
# 	h=float(input("Enter height:"))
# 	print(f"Area of triangle is:{calculate_triangle_area(b,h)}")


#######ceaser cipher

# def getDoubleAlphabet(alphabet):
#     doubleAlphabet = alphabet + alphabet
#     return doubleAlphabet

# def getMessage():
#     stringToEncrypt = input("Please enter a message to encrypt: ")
#     return stringToEncrypt

# def getCipherKey():
#     shiftAmount = input( "Please enter a key (whole number from 1-25): ")
#     return shiftAmount

# def decryptMessage(message, cipherKey, alphabet):
#     decryptKey = -1 * int(cipherKey)
#     return encryptMessage(message, decryptKey, alphabet)

# def encryptMessage(message, cipherKey, alphabet):
#     encryptedMessage = ""
#     uppercaseMessage = ""
#     uppercaseMessage = message.upper()
#     for currentCharacter in uppercaseMessage:
#         position = alphabet.find(currentCharacter)
#         newPosition = position + int(cipherKey)
#         if currentCharacter in alphabet:
#             encryptedMessage = encryptedMessage + alphabet[newPosition]
#         else:
#             encryptedMessage = encryptedMessage + currentCharacter
#     return encryptedMessage

# def runCaesarCipherProgram():
#     myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     print(f'Alphabet: {myAlphabet}')
#     myAlphabet2 = getDoubleAlphabet(myAlphabet)
#     print(f'Alphabet2: {myAlphabet2}')
#     myMessage = getMessage()
#     print(myMessage)
#     myCipherKey = getCipherKey()
#     print(myCipherKey)
#     myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
#     print(f'Encrypted Message: {myEncryptedMessage}')
#     myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
#     print(f'Decypted Message: {myDecryptedMessage}')
    
#     runCaesarCipherProgram()

