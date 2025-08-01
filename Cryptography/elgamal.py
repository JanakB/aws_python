p = int(input("Enter a prime number(p):"))
g = int(input("Enter a primite root of p (g):"))
x =int(input("Enter x  "))
y = (g**x)%p

def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i


choice = int(input("Enter 1 for encode and 2 for decode:"))
if(choice==1):
    pt = int(input("Enter pt(in number) to encode:"))
    k =int(input("Enter k such that 1<x<p-2:"))
    c1 = (g**k)%p
    c2 = (pt*(y**k))%p
    print(f"Cipher text = ({c1},{c2})")
elif(choice ==2):
    c1 = int(input("Enter ct1 to decode:"))
    c2 = int(input("Enter ct2 to decode:"))
    temp = (c1**x)%p
    pt =(c2*(mod_Inv(temp,p)))%p
    print(f"Plaintext:{pt}")
else:
    print("Wrong choice")
