p = int(input("Enter a prime number(p):"))
q = int(input("Enter a prime number(q):"))
n = p*q
tot_n = (p-1)*(q-1) 
e =int(input(f"Enter e such that gcd(e,{tot_n}) =1 and 1<e<{tot_n}:)"))
def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i
d = mod_Inv(e,tot_n)

choice = int(input("Enter 1 for encode and 2 for decode:"))
if(choice==1):
    pt = int(input("Enter pt(in number) to encode:"))
    ct =(pt**e)%n
    print("Ciphertext:"+str(ct))
elif(choice ==2):
    ct = int(input("Enter ct(in number) to decode:"))
    pt =(ct**d)%n
    print("Plaintext:"+str(pt))
else:
    print("Wrong choice")
