# user_input = int(input("Enter a number: "))
# even_count = 0
# for num in range(1, user_input + 1):
#     if num % 2 == 0:
#         even_count += 1
# print(f"The number of even numbers between 1 and {user_input} is: {even_count}")

#wap to calculate sum of first 50 even numbers.
#wap to find the factorial of any number.
#wap to find multiplication factor of any provided by user 
#wap to show the division of percentage obtained by a student.
#wap to show different formating styles in python.
#can you use switch case in python?
#wap to check if a given number is palindrome or not.
#wap to take a string and check if the string is ram.



##prime number
# user_input = int(input("Enter a number: "))
# for num in range(1, user_input + 1):
#    Prime_count = 0
#    for i in range(2,user_input):
#         if num % i == 0:
#             Prime_count += 1
#         print(f"The number of prime numbers between 1 and {user_input} is: {Prime_count}")


######square of first 10 prime number
# count=0
#sum=0
#while count<10:
#num=num+1
#     if num > 1:
#         for i in range(2, int(num**0.5)+1):
#             if(num % i) == 0:
#                 print(f"{num} is not a prime number")
#                 break
#             else:
#                 count = count+1
#                 print(f"{count} {num} is a prime number and square is : {num*num}")
#         else:
#             print(f"{num} is not a prime number")
#     print(count)                


# #wap to calculate sum of first 50 even numbers.
# sum = 0
# for num in range(0,101):
#  if num % 2 == 0:
#      sum = sum + num
#      print("the sum of first 50 even number",sum )

## factorial

# num = int(input("enter a number:"))
# factorial=1
# for i in range(num,0,-1):
#     factorial=factorial*i
    
# print(factorial)

# #sum of first 65 prime number
# c=0
# count=0
# r=int(input("enter range:"))
# for i in range(1,r):
#     for j in range(1,i+1):
#         if i%j == 0:
#             c=c+1
#     if c==2:
#         count+=1
#     c=0
# print(count)    

#to check string is ram

# string = input("enter a string:")
# if string == "ram":
#     print("the string is correct")
# else:   
#     print("string is incorrect")         

# #multiplication factor
# num = int(input("enter any number:"))
# for i in range(1,num+1):
#     if num % i == 0:
#         print(f" multipaction factor of {num} is {i}")

# #### percentage division of students
# total = 0
# for i in range(0,5):
#     input("enter name of student:")
#      num = int(input("enter the number:"))
#      total=total+num
#      percentage = total/500
#      print("percentage is:",percentage)    
#          if percentage >=60:
#         print("You secure first division")
#     else:
#         if percentage >=80:
#             print("you secure descrition")
#     else:
#         if percentage < 50:
#         print("very low marks pls work hard")

#### palindrome or not

# j = input("enter the value:")
# reverse= j[::-1]
# if(reverse == j):
#     print("it is palindrome")
# else:
#     print("not palindrome")



###

# import copy

# original_lst = [1,2,3,[4,2,1]]

# normal_copy =original_lst.copy()
# deep_copy = copy.deepcopy(original_lst)

# original_lst[3][0] =33

# print("original list",original_lst)
# print("normal copy",normal_copy)
# print("deep copy",deep_copy)

###square of list
# lst=[1,2,3,4,5,6,6]

# lst2 = [x**2 for x in lst]
# print(lst2)
