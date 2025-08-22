def main(Z,a,c,m):
    X = 0
    X= (Z*a+c) % m
    return X

if "__main__" == __name__:
    arr = []
    choice = input("Enter\na. Additive.\nb. Multiplcative.\nc. Mixed.\nd. Exit.\n")
    print("\n")
    if choice == 'a':
        c = int((input("Enter increament: ")))
        a=1

    elif choice == 'b':
        a = int(input(("Enter multiplier: " )))
        c=0

    elif choice == 'c':
        a = int(input(("Enter multiplier: " )))
        c = int((input("Enter increament: ")))

    else:
        print("Error")
        exit(0)

    Z = int(input("Enter initial seed: "))
    m = int(input("Enter modulo: "))
    n = 0

    while(n<m):
        Z = main(Z,a,c,m)
        arr.append(Z)
        print(f"{n} tries: {Z}")
        n+=1