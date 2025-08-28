from math import floor, sqrt

#Test for 3rd, 8th, 13th and so on
arr = [0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
       0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
       0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87]

i = 3 # beginning with 3rd number
arr1 = [i]
m = 5 # every 5 numbers
N = 30 # total 30 numbers
a = 0
critical_value = 1.96

M= floor((N-i)/m-1)

for j in range(M+1):
    arr1.append(i+(j+1)*m)

for k in range(len(arr1)-1):
    a = a + arr[arr1[k]-1]*arr[arr1[k+1]-1]

r = (a/(M+1))-0.25

alpha = sqrt(13*M+7) / (12 * (M+1))

tabulated_value = r/alpha

print("Result=", tabulated_value)
if(tabulated_value < critical_value):
     print("Null hypothesis is accepted")
else:
     print("Null hypothesis is rejected")

