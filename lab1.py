# print("Hello world !")
# a = 5
# b = 6
# print(a+b)
# print(" I am Janak")

# print("What is your name?")

# print("My name is Janak")

# print("janak \n"*10)

# name = input("Enter your name:")
# print("my name is",name)

# age = input("enter your age:")
# print("age =",age)

# email = input("enter email address:")
# print("email id=",email)

# proffession = input("who you are:")
# print("I am",proffession)

# faculty = input ("which faculty do you read:")
# print(" I read in",faculty) 

# prime_number = input("enter any 5 prime number:")
# print("any 5 prime number are:", prime_number)

# odd_number = input ("enter 5 odds number:")
# print("5 odd number are:", odd_number)

# age = (input("enter your age:"))
# print("your age is:",type(age))

# age = int(input("Enter your age:"))
# print("your age is:",type(age))

# birth_year = int(input("enter your birth year:\n"))
# pyear = int(input("enter your birth year"))

# age = pyear - birth_year
# print("your are ",age)

# user_input = int(input("enter any one number:"))

# if user_input > 100:    
#     print("greater than 100")
# elif user_input == 100:
#     print("equal")
# else:
#     print("less than 100")

#### for loop range

# for i in range(10):
#     print(i)

# marks1 = int(input("enter marks of science subject:"))
# print("science ",marks1)

# marks2 = int(input("enter marks of social subject:"))
# print("social ",marks2)

# marks3 = int(input("enter marks of eph subject:"))
# print("eph",marks3)

# marks4 = int(input("enter marks of computer subject:"))
# print("computer ",marks4)

# marks5 = int(input("enter marks of english subject:"))
# print("english ",marks1)

# total_marks = int(print(marks1+marks2+marks3+marks4+marks5))

# percentage = int(print(total_marks/500 * 100))
# ####percentage of 5 subject
# total = 0
# for i in range(0,5):
#     num = int(input("enter the number:"))
#     total=total+num
#     percentage = total/500
#     print("percentage is:",percentage)    

####multiplication table of 13

# for i in range (1,13):
#     print(f"13*{i}=",13*i)
    
# #######formating
# name='janak'
# age=24
# print(f"hello my name is {name} i am {age} years old")
# print("hello my name is {} i am {} years old".format(name,age))
# # print("hello my name is",name, "i am",age,"years old")    

# name = 'Janak'
# age = 28
# study = 'Csit'
# address = 'Basundhara'
# print(f"hello I am {name} I am {age} year old I study {study} I am from {address}")


#####Ascii

# print(ord("A"))
# print(chr(65))


### write a program to find Ascii values of your name

# name = input("Enter your name:")
# for char in name:
#     print(ord(char))
    
    
####Wap to find area of a circle,rectangle,volume of the cube and find square of first 10 prime numbers.

# length = int(input("enter the length:"))
# breadth = float(input("enter the breadth:"))
# area_rectangle = print(length*breadth)
# print(f"area of rectangle is: {area_rectangle}")

# radius = float(input("enter the radius:"))
# pi = 3.14
# area_circle = print(pi*radius*radius)
# print(f"area of circle is: {area_circle}")

# length_c = float(input("enter the length of cube:"))
# volume = print(length_c*length_c*length_c)
# print(f"volume of cube is:{volume}")

# # ## square of first 10 prime number
# c=0
# count=0
# r=int(input("enter range:"))
# for i in range(1,r):
#      for j in range(1,i+1):
#          if i%j == 0:
#              c=c+1
#      if c==2:
#          count+=1
#      c=0
# print(i*i)

###2 square of first 10 prime number
# count=0
# # sum=0
# num=0
# while count<10:
#     num=num+1
#     if num > 1:
#         for i in range(2, int(num**0.5)+1):
#             if(num % i) == 0:
#                 print(f"{num} is not a prime number")
#                 break
#         else:
#                 count = count+1
#                 print(f" {num} is a prime number and square is : {num*num}")
#     else:
#             print(f"{num} is not a prime number")
#     # print(count)

# #####s: Write a program that prompts the user to enter their
# name and their favorite color. Then, create a message that
# combines their name and favorite color to form a personalized
# message. Finally, print the message on the console
##1
# name = input("enter your name:")
# color = input("enter favorite collor:")
# print(f"my name is {name} and my favorite color is {color}")
            

##Question 2: Write a program that prompts the user to enter a
# sentence. Count and display the number of words in the
# sentence.

# sentence = "hi i am 3rd cohrt of aws"
# split=sentence.split(" ")
# print(len(split))

# ###2
# user_input =input("enter any sentences:")
# print(len(splited =user_input.split(" ")))

# ####Question 3: Write a program that prompts the user to enter their
# full name (first name and last name). Convert the name to
# uppercase and display it in reverse order with a comma
# separating the last name and the first name.

# full= input("enter full name:")
# print(full.upper())
# split =full.split(" ")
# firstname =[0]
# lastname =[1]
# print(firstname)
# print(lastname)
# print(f"{lastname.upper()}, {firstname.upper()}")
# rev = "Janak,Budhathoki"[::-1]
# print(rev)

# Question 4: Write a program that takes a sentence as input and
# replaces all occurrences of a specific word with another word.
# Prompt the user to enter the original sentence, the word to be
# replaced, and the replacement word. Display the modified
# sentence.

#user_in =input("enter a sentence:")
# sent = "I am student of csit i have been reading csit since few year"
# rep= sent.replace("csit","unlimited")

# modified=print(rep)


# ###2
# user_inp = input("enter a sentence:")
# rword = input("which word u want to replace:")
# replaced_word = input(f"you want to replace {rword} with ?:")
# new_sent = user_inp.replace(rword,replaced_word)
# print(new_sent)

####list
# my_list = [1000,'potato','Medicine',1.2,'tomato']
# print(my_list)
# print(my_list[1])
# popped_val = my_list.pop(1)
# print(popped_val)
# my_list.insert(3,"phone")
# my_list.append("masala")
# my_list.remeove(2)

# list1=[1,2,7,3,9,8,6,3,4]
# list1.sort()#ascending order
# print(list1)
# list1.sort(reverse=True)#descending 
# list1.clear()#clear

# # Create a list named "numbers" containing the numbers 1, 3,
# 5, 7, and 9.
# 2. Access and print the second element of the list.
# 3. Modify the third element of the list to 10.
# 4. Add the number 12 to the end of the list.
# 5. Remove the nurember 5 from the list.
# 6. Create a new list named "sliced_list" that contains a slice of
# the original list from the second to the fourth element.
# 7. Create a new list named "combined_list" by concatenating
# the original list with the sliced_list.
# 8. Check if the number 8 is present in the combined_list and
# print the result.
# 9. Sort the combined_list in ascending order.
# 10. Print the final version of the combined_list.

# numbers = [1,3,5,7,9]
# print(numbers[1])
# # numbers[2] =10
# # print(numbers)
# numbers.append(12)
# print(numbers)
# # numbers.remove(5)
# print(numbers)
# sliced_list =numbers[1:5]
# print(sliced_list)

# combined_list=numbers+sliced_list
# print(combined_list)
# if 8 in combined_list:
#   print("8 in combined_list")
# else:
#     print("8 is not in list")
    
# combined_list.sort()
# print(combined_list)    
    
    
    
#     ###tuples
# tuple = (1,2,3,4,2,4,2,3,2)
# count_1 = tuple.count(2)#count
# print(tuple)
# print(min(tuple))#minimum value check
# sr =sorted(tuple)#sort ascending order
# print(sr)

# ####1. Define a tuple named my_tuple with the following elements: 10,
# 20, 'a', 'b', True.
# 2. Write the code to access and print the third element of the tuple
# my_tuple.
# 3. Concatenate two tuples: tuple1 with elements (1, 2, 3) and tuple2
# with elements ('x', 'y', 'z'). Store the result in a new tuple called
# concatenated_tuple.
# 4. Write a Python code snippet to repeat the tuple my_tuple three
# times and store the result in a new tuple named repeated_tuple.
# 5. Determine the length of the tuple concatenated_tuple using a
# built-in function and print the result.
# 6. Perform slicing on the tuple my_tuple to extract a new tuple with
# elements 'a', 'b', and True. Store the result in a variable called
# # sliced_tuple.

# my_tuple = (10,20,'a','b',True)
# print(my_tuple)
# print(my_tuple[3])
# tuple1=(1,2,3)
# tuple2=('X','Y','z')
# concatened_tuple=tuple1+tuple2
# print(concatened_tuple)
# repeated_tuple = my_tuple*3
# print(repeated_tuple)
# print(len(concatened_tuple))
# sliced_tuple = my_tuple[2::]
# print(sliced_tuple) 
# tuplelist=list(my_tuple)#conversion tuple to list
# print(tuplelist)
# print(type(tuplelist))


#####dist

# my_dist = {
#     "Name": "ashok",
#      "age":23,
#      "address":"kathmandu"
# }

# a = my_dist["name"]
# print(a) 

# info = {
#     'name':'janak',
#     'age': 33,
#     'eligible':True
# }
# print(info)
# print(info.keys())
# print(info.values())
# for key in info.keys():
#     print(f"the value corresponding to the key {key} is {info[key]} ")

# ##wap to find square of every elements of list and find the sum.
# new_list =[2,5,7,9,6]
# print(new_list)
# temp_list=[]
# sum=0
# for i in new_list:
#     temp_list.append(i*i)
#     sum=sum+(i*i)
#     print(temp_list)
#     print(sum)


## Wap to check if a given string is present in list or not.
# list1 = [1,2,3,4,5,6,'janak']
# if 'janak' in list1:
#     print('given string is in the list')
# else:
#     print('given string is not in the list')
# # wap to copy list elements into another list.(both list should be independent) 
# newlist = list1[::]
# print(new_list)
# new_list.append("hari")
# print(list1)
# print(new_list)

####wap to take input of combination of character a,b,c in any order given that a=20 b=18 c=22 now find the 
# total weight for the combination of character

# dict_val ={"A":20,"B":18,"C":22}
# a=input ("enter the characters:")
# print((a.count("A")*dict_val["A"])+(a.count("B")*dict_val["B"])+(a.count("C")*dict_val["C"]))

# var = input("enter characters:")
# a= var.upper()
# print(a)
# print((var.count("A")*20)+(var.count("B")*18)+(var.count("C")*22))

#####random number

# import random
# for i in range(100):
#    rnum=random.randint(1,33)
#    print(rnum)
   
   
# dict_val ={'A':20,'B':33,'C':22}
# print(type(dict_val))

   ### wap to find simple interest 
# def simple(p,t,r):
#  return((p*t*r)/100)
# print(simple(1000,3,12))


   ### wap to check if given number is prime or not
# def prime():
  
#    num = int(input("enter any number:"))
#    for i in range(2, int(num**0.5)+1):
#         if(num % i) == 0:
#                 print(f"{num} is not a prime number")
#                 break
#    else:
#               print("number is prime")
      

# prime()  

    
   ### wap to calculate weight of given number
   
   ## wap to define 5 user define function in same program
# def calcu(a,b):
#    return(a+b)
# print(calcu(2,3))
# def mul(a,b):
#    return(a*b)
# print(mul(4,5))
# def div(a,b):
#    return(a/b)
# print(div(7,2))
# def sub(a,b):
#    return(a-b)
# print(sub(6,2))
# def mod(a,b):
#    return(a%b)
# print(mod(8,3))

 
#    ## wap to show use case of different types of function
# def nopa():
#    print("hello world")

# def functionn1():
#    a=3
#    b=4
#    return(a+b)
# print(functionn1())

# def function2(a,b):
#    return(a+b)
# print(function2(5,9))


# def function3(c=3,d=4):
#    sum=c+d
#    print(sum)
# function3()
   
   ## wap to count numbers of square numbers betn 50 and 929.
# def square():
#    count=0
#    for num in range(50,929):
#       temp=num**0.5
#       if (int(temp)**2)==num:
#          print(num)
#          count+=1
#    print(f"total perfect square is:",count)
# square()



#    ## wap to sum digits provided by the user.
# def sum_digit():
#    sum=0
#    a= input("enter any number:")
#    for i in a:
#       sum=sum+int(i)
#    return(sum)

# print(sum_digit())
   
   ###wap to calculate body mass index
    ##convert 3 years 12 months 4 days 21 hours 52min 20sec into sec
    ###convert 8290000mins into year month day hr min