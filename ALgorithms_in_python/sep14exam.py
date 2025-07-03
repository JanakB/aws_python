# import random

# list1=[2,4,8,9,10,11,1]

# list2=[]

# while len(list2)<7:
# 	var=random.choice(list1)
# 	if var in list2:
# 		continue
# 	else:
# 		list2.append(var)
# 	# print(list2)

# print(list2)


#2.
# dict1={
# 	"key1":"val1",
# 	"key1":"val2"
# }

# print(dict1)

#3.
# tuple1=(44,4,5,6,7)
# print(tuple1[0])
# print("type(tuple1)")
# tlist=list(tuple1)
# print(tlist)
# for i in range(len(tlist)):
# 	tlist[i]=int(tlist[i]*tlist[i])
# tuple2=tuple(tlist)
# print(tuple2)
# print(type(tuple2))

#4:
# def funcube(num):
# 	temp=num**(1/3)
# 	if (int(temp)**3 == num):
# 		print(f"{num} is perfect cube")
# 	else:
# 		print(f"{num} is NOT perfect cube")
# num=int(input("Enter a number:"))	
# funcube(num)

#5:
# list1=[13,2,3,40,4,5]
# list2=[3,4,5,6,7,8,34]
# list3=list1+list2
# print(f"Minimum value: {min(list3)}")
# print(f"Maximum value: {max(list3)}")

#6:

# string=input("Enter a string:")
# upper=[]
# lower=[]
# for char in string:
# 	if char == " ":
# 		continue
# 	if char.isupper()==True:
# 		upper.append(char)
# 	else:
# 		lower.append(char)

# print(upper)
# print(lower)


#7:

# list1=[3,4,5,6,7]

# table=[]
# for i in list1:
# 	list2=[]
# 	for j in range(1,11):
# 		# print(f"{i}x {j}")
# 		list2.append(i*j)
# 	# print(list2)
# 	table.append(list2)
# print(table)


#8:
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


#9:
# d=33
# C=29*d
# b=16*C
# A=20*b
# a=20*A
# print(a*a*b*A*C*d*C*A)


#10:

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