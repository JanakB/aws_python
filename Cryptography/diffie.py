def isPrimitiveRootof(a,q):
    countindex = q-1
    result = [] 
    while(countindex>0):
        response = (a**countindex % q)
        result.append(response)
        countindex -= 1
    result.sort()
    expected_result = list(range(1,q))  
    if result==expected_result:
        print(f"Expected result: {expected_result}")
        print(f"Result : {result}")
        print("Primite root")
        return True
    else:
        return False

    
#private key denoted by X and public key is denoted by Y
q = int(input("Enter q:"))
alpha = int(input("Enter alpha:"))

if isPrimitiveRootof(alpha,q):
    if alpha<q:
        pass
    else: 
        print(f"{alpha} is smaller than {q}")
else:
    print(f"{alpha} is not primitive root of {q}")
    exit()

pvA = int(input("Enter an assumed private key for A(A<q):"))
pubA = (alpha**pvA)%q

pvB = int(input("Enter an assumed private key for B(B<q):"))
pubB = (alpha**pvB)%q

# Calculating key for  A
keyA = (pubB**pvA)%q

# Calculating key for  B
keyB = (pubA**pvB)%q


#check if key of A and key of B match

print(f"Key of A {keyA}")
print(f"Key of B {keyB}")


if(keyA==keyB):
    print("Keys are identical")