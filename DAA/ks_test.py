def ks_test(arr, num):
    critical_value = 0.565 
    D_plusminus = []
    for i in range(num):
        plus = (i+1)/num - arr[i]
        minus = arr[i] - (i/num) 
        D_plusminus.append(plus)
        D_plusminus.append(minus)

    tabulated_value = max(D_plusminus) 
    print("Result: ", tabulated_value) 
    if(tabulated_value < critical_value):
        print("Null hypothesis is accepted")

    else:
        print("Null hypothesis is rejected")

num = int(input("Enter the total number of random numbers."))

arr = []
print("Enter numbers in ascending order: ")
for i in range(num):
    ele = float(input())
    arr.append(ele)

ks_test(arr, num)